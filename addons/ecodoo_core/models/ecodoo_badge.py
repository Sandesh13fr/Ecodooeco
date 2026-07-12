from odoo import api, fields, models, _


class EcodooBadge(models.Model):
    _name = 'ecodoo.badge'
    _description = 'Employee Badge'
    _order = 'xp_threshold desc'
    _rec_name = 'name'

    name = fields.Char(required=True)
    description = fields.Text()
    xp_threshold = fields.Integer(
        string='XP Threshold',
        required=True,
        default=0,
        help='Minimum XP required to earn this badge',
    )
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        'res.company',
        required=True,
        default=lambda self: self.env.company,
    )


class EcodooEmployeeBadge(models.Model):
    _name = 'ecodoo.employee.badge'
    _description = 'Employee Badge Award'
    _order = 'awarded_at desc'
    _rec_name = 'display_name'

    employee_id = fields.Many2one(
        'hr.employee',
        required=True,
        ondelete='cascade',
    )
    badge_id = fields.Many2one(
        'ecodoo.badge',
        required=True,
        ondelete='cascade',
    )
    awarded_at = fields.Datetime(default=fields.Datetime.now, required=True)
    source_participation_id = fields.Many2one(
        'ecodoo.challenge.participation',
        string='Source Participation',
        ondelete='set null',
    )
    company_id = fields.Many2one(
        'res.company',
        required=True,
        default=lambda self: self.env.company,
    )
    display_name = fields.Char(compute='_compute_display_name', store=True)

    _sql_constraints = [
        ('employee_badge_unique',
         'UNIQUE(employee_id, badge_id)',
         'An employee can only earn a badge once.'),
    ]

    @api.depends('employee_id', 'badge_id')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f'{record.employee_id.name} - {record.badge_id.name}'


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    ecodoo_xp = fields.Integer(
        string='EcoDoo XP',
        default=0,
        help='Total XP earned from challenges',
    )