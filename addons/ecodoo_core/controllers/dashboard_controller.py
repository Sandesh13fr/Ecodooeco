# -*- coding: utf-8 -*-
"""Dashboard API Controller"""
from odoo import http
from odoo.http import request
import json


class EcodooDashboardController(http.Controller):
    """JSON API endpoint for EcoDoo Dashboard"""

    @http.route('/api/v1/ecodoo/dashboard', type='json', auth='user', methods=['POST'], csrf=False)
    def get_dashboard_data(self, **kwargs):
        """Return dashboard data as JSON"""
        # Ensure user has access to ecodoo dashboard
        if not request.env.user.has_group('ecodoo_core.group_ecodoo_employee'):
            return {'error': 'Access denied'}
        
        dashboard = request.env['ecodoo.dashboard']
        data = dashboard.get_dashboard_data()
        return data

    @http.route('/api/v1/ecodoo/dashboard/public', type='json', auth='public', methods=['POST'], csrf=False)
    def get_public_dashboard_data(self, **kwargs):
        """Public endpoint for embedded dashboards (limited data)"""
        # This would require API key authentication in production
        # For now, return minimal data
        return {
            'total_co2e': 0.0,
            'environmental_score': 0.0,
            'social_score': 0.0,
            'governance_score': 0.0,
            'overall_score': 0.0,
            'data_freshness': '',
            'score_disclaimer': 'Demonstration management score; not a reporting standard or assurance result.',
        }