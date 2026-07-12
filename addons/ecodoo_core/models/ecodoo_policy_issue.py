from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class EcodooPolicy(models.Model):
    _name = 'ecodoo.policy'
    _description = 'ESG Policy'
    _order = 'effective_date desc'
    _rec_name = 'display_name'

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    version = fields.Char(required=True, default='1.0')
    body = fields.Html(string='Content')
    owner_id = fields.Many2one('res.users', string='Owner')
    effective_date = fields.Date()
    review_date = fields.Date()
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('published', 'Published'),
            ('archived', 'Archived'),
        ],
        default='draft',
        required=True,
    )
    company_id = fields.Many2one(
        'res.company',
        required=True,
        default=lambda self: self.env.company,
    )
    display_name = fields.Char(compute='_compute_display_name', store=True)

    _sql_constraints = [
        ('code_version_company_unique',
         'UNIQUE(code, version, company_id)',
         'Policy code, version, and company must be unique.'),
    ]

    @api.depends('name', 'code', 'version')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f'{record.name} ({record.code} v{record.version})'

    def action_publish(self):
        for record in self:
            if record.state != 'draft':
                raise UserError(_('Can only publish from Draft state.'))
            record.state = 'published'

    def action_archive(self):
        for record in self:
            if record.state != 'published':
                raise UserError(_('Can only archive from Published state.'))
            record.state = 'archived'

    @api.constrains('state', 'name', 'code', 'version', 'body', 'owner_id', 'effective_date', 'review_date')
    def _check_published_immutable(self):
        for record in self:
            if record.state == 'published' and record._origin.state == 'published':
                changed_fields = []
                for field_name in ['name', 'code', 'version', 'body', 'owner_id', 'effective_date', 'review_date']:
                    if record[field_name] != record._origin[field_name]:
                        changed_fields.append(field_name)
                if changed_fields:
                    raise ValidationError(_(
                        'Published policies are immutable. Cannot change: %s',
                        ', '.join(changed_fields)
                    ))


class EcodooPolicyAcknowledgement(models.Model):
    _name = 'ecodoo.policy.acknowledgement'
    _description = 'Policy Acknowledgement'
    _rec_name = 'display_name'

    policy_id = fields.Many2one(
        'ecodoo.policy',
        required=True,
        ondelete='cascade',
    )
    employee_id = fields.Many2one(
        'hr.employee',
        required=True,
    )
    acknowledged_at = fields.Datetime(default=fields.Datetime.now, required=True)
    company_id = fields.Many2one(
        'res.company',
        required=True,
        default=lambda self: self.env.company,
    )
    display_name = fields.Char(compute='_compute_display_name', store=True)

    _sql_constraints = [
        ('policy_employee_unique',
         'UNIQUE(policy_id, employee_id)',
         'An employee can only acknowledge a policy once.'),
    ]

    @api.depends('policy_id', 'employee_id')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f'{record.policy_id.name} - {record.employee_id.name}'

    @api.constrains('policy_id')
    def _check_policy_published(self):
        for record in self:
            if record.policy_id.state != 'published':
                raise ValidationError(_('Can only acknowledge published policies.'))


class EcodooComplianceIssue(models.Model):
    _name = 'ecodoo.compliance.issue'
    _description = 'Compliance Issue'
    _order = 'severity desc, due_date asc'
    _rec_name = 'name'

    name = fields.Char(required=True)
    severity = fields.Selection(
        selection=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
            ('critical', 'Critical'),
        ],
        required=True,
        default='medium',
    )
    description = fields.Text()
    owner_id = fields.Many2one('res.users', string='Owner')
    due_date = fields.Date()
    resolution = fields.Text()
    state = fields.Selection(
        selection=[
            ('open', 'Open'),
            ('in_progress', 'In Progress'),
            ('resolved', 'Resolved'),
        ],
        default='open',
        required=True,
    )
    resolved_at = fields.Datetime()
    company_id = fields.Many2one(
        'res.company',
        required=True,
        default=lambda self: self.env.company,
    )

    def action_in_progress(self):
        for record in self:
            if record.state != 'open':
                raise UserError(_('Can only move to In Progress from Open state.'))
            record.state = 'in_progress'

    def action_resolve(self):
        for record in self:
            if record.state != 'in_progress':
                raise UserError(_('Can only resolve from In Progress state.'))
            if not record.resolution:
                raise UserError(_('Resolution is required to resolve the issue.'))
            record.state = 'resolved'
            record.resolved_at = fields.Datetime.now()

    def action_reopen(self):
        for record in self:
            if record.state != 'resolved':
                raise UserError(_('Can only reopen from Resolved state.'))
            record.state = 'open'
            record.resolved_at = False