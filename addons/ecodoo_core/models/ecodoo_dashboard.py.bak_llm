from odoo import api, fields, models, _
from odoo.tools import float_round
from datetime import datetime


class EcodooDashboard(models.Model):
    _name = 'ecodoo.dashboard'
    _description = 'EcoDoo Dashboard Data'

    @api.model
    def get_dashboard_data(self):
        """Return dashboard data as JSON-serializable dict"""
        company = self.env.company
        today = fields.Date.today()
        now_iso = fields.Datetime.now().isoformat()

        # Total CO2e from posted transactions
        domain = [
            ('state', '=', 'posted'),
            ('company_id', '=', company.id),
        ]
        transactions = self.env['ecodoo.carbon.transaction'].search(domain)
        total_co2e = sum(transactions.mapped('kg_co2e'))

        # Environmental Score
        env_score = self._compute_environmental_score(company)

        # Social Score
        social_score = self._compute_social_score(company)

        # Governance Score
        gov_score = self._compute_governance_score(company)

        # Overall Score
        overall_score = float_round(0.4 * env_score + 0.3 * social_score + 0.3 * gov_score, 2)

        # Active goal count
        active_goal_count = self.env['ecodoo.goal'].search_count([
            ('state', '=', 'active'),
            ('company_id', '=', company.id),
        ])

        # Open issue count
        open_issue_count = self.env['ecodoo.compliance.issue'].search_count([
            ('state', '=', 'open'),
            ('company_id', '=', company.id),
        ])

        # Approved participation count
        approved_participation_count = self.env['ecodoo.challenge.participation'].search_count([
            ('state', '=', 'approved'),
            ('company_id', '=', company.id),
        ])

        # Employee count (active)
        employee_count = self.env['hr.employee'].search_count([
            ('company_id', '=', company.id),
            ('active', '=', True),
        ])

        # Department series
        dept_series = self._get_department_series(company)

        # Recent transactions (last 5)
        recent_transactions = self._get_recent_transactions(company)

        return {
            'total_co2e': float_round(total_co2e, 2),
            'environmental_score': float_round(env_score, 2),
            'social_score': float_round(social_score, 2),
            'governance_score': float_round(gov_score, 2),
            'overall_score': float_round(overall_score, 2),
            'active_goal_count': active_goal_count,
            'open_issue_count': open_issue_count,
            'approved_participation_count': approved_participation_count,
            'employee_count': employee_count,
            'department_series': dept_series,
            'recent_transactions': recent_transactions,
            'data_freshness': now_iso,
            'score_disclaimer': 'Demonstration management score; not a reporting standard or assurance result.',
        }

    def _compute_environmental_score(self, company):
        """Environmental = average over active goals of (100 if actual≤target else max(0, target/actual×100)); 0 if no active goal"""
        goals = self.env['ecodoo.goal'].search([
            ('state', '=', 'active'),
            ('company_id', '=', company.id),
        ])
        if not goals:
            return 0.0
        scores = []
        for goal in goals:
            if goal.actual_kg_co2e <= goal.target_kg_co2e:
                scores.append(100.0)
            else:
                ratio = goal.target_kg_co2e / goal.actual_kg_co2e * 100
                scores.append(max(0.0, ratio))
        return sum(scores) / len(scores) if scores else 0.0

    def _compute_social_score(self, company):
        """Social = approved unique employee participations / active employee count × 100, capped 100"""
        active_employees = self.env['hr.employee'].search([
            ('company_id', '=', company.id),
            ('active', '=', True),
        ])
        if not active_employees:
            return 0.0

        participations = self.env['ecodoo.challenge.participation'].search([
            ('state', '=', 'approved'),
            ('company_id', '=', company.id),
        ])
        unique_employees = set(participations.mapped('employee_id').ids)
        rate = len(unique_employees) / len(active_employees) * 100
        return min(100.0, rate)

    def _compute_governance_score(self, company):
        """Governance = 50×acknowledgement_rate + 50×issue_resolution_rate
        ack_rate = acknowledgements for published policies / (published policies × active employees)
        resolution_rate = resolved issues / all issues
        missing denominator = 0 for that half
        """
        # Acknowledgement rate
        published_policies = self.env['ecodoo.policy'].search([
            ('state', '=', 'published'),
            ('company_id', '=', company.id),
        ])
        active_employees = self.env['hr.employee'].search([
            ('company_id', '=', company.id),
            ('active', '=', True),
        ])

        if published_policies and active_employees:
            ack_count = self.env['ecodoo.policy.acknowledgement'].search_count([
                ('policy_id', 'in', published_policies.ids),
                ('company_id', '=', company.id),
            ])
            ack_denominator = len(published_policies) * len(active_employees)
            ack_rate = ack_count / ack_denominator if ack_denominator > 0 else 0.0
        else:
            ack_rate = 0.0

        # Issue resolution rate
        all_issues = self.env['ecodoo.compliance.issue'].search([
            ('company_id', '=', company.id),
        ])
        if all_issues:
            resolved_count = len(all_issues.filtered(lambda i: i.state == 'resolved'))
            resolution_rate = resolved_count / len(all_issues)
        else:
            resolution_rate = 0.0

        return 50.0 * ack_rate + 50.0 * resolution_rate

    def _get_department_series(self, company):
        """Get CO2e by department"""
        domain = [
            ('state', '=', 'posted'),
            ('company_id', '=', company.id),
        ]
        transactions = self.env['ecodoo.carbon.transaction'].search(domain)
        dept_data = {}
        for txn in transactions:
            dept_name = txn.department_id.name or 'Unknown'
            dept_data[dept_name] = dept_data.get(dept_name, 0.0) + txn.kg_co2e
        return [
            {'department': dept, 'kg_co2e': float_round(val, 2)}
            for dept, val in sorted(dept_data.items(), key=lambda x: x[1], reverse=True)
        ]

    def _get_recent_transactions(self, company, limit=5):
        """Get last 5 posted transactions"""
        domain = [
            ('state', '=', 'posted'),
            ('company_id', '=', company.id),
        ]
        transactions = self.env['ecodoo.carbon.transaction'].search(
            domain, order='activity_date desc, id desc', limit=limit
        )
        return [
            {
                'id': txn.id,
                'name': txn.name,
                'department': txn.department_id.name or '',
                'kg_co2e': float_round(txn.kg_co2e, 2),
                'activity_date': txn.activity_date.isoformat() if txn.activity_date else '',
            }
            for txn in transactions
        ]