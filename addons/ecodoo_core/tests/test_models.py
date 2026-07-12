# -*- coding: utf-8 -*-
"""Test for ecodoo_core models"""
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError, UserError
from odoo.tools import float_round


class TestEmissionFactor(TransactionCase):
    """Test ecodoo.emission.factor model"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = cls.env.company
        cls.uom_litre = cls.env.ref('uom.product_uom_litre')

    def test_create_factor(self):
        """Test creating a draft emission factor"""
        factor = self.env['ecodoo.emission.factor'].create({
            'name': 'Test Diesel',
            'code': 'DIESEL-TEST',
            'activity_type': 'fuel',
            'input_uom_id': self.uom_litre.id,
            'kg_co2e_per_unit': 2.5,
            'version': '1.0',
            'company_id': self.company.id,
        })
        self.assertEqual(factor.state, 'draft')
        self.assertEqual(factor.kg_co2e_per_unit, 2.5)

    def test_approve_factor(self):
        """Test approving a factor"""
        factor = self.env['ecodoo.emission.factor'].create({
            'name': 'Test Diesel',
            'code': 'DIESEL-TEST',
            'activity_type': 'fuel',
            'input_uom_id': self.uom_litre.id,
            'kg_co2e_per_unit': 2.5,
            'version': '1.0',
            'company_id': self.company.id,
        })
        factor.action_approve()
        self.assertEqual(factor.state, 'approved')

    def test_approved_factor_immutable(self):
        """Test that approved factors cannot be modified"""
        factor = self.env['ecodoo.emission.factor'].create({
            'name': 'Test Diesel',
            'code': 'DIESEL-TEST',
            'activity_type': 'fuel',
            'input_uom_id': self.uom_litre.id,
            'kg_co2e_per_unit': 2.5,
            'version': '1.0',
            'company_id': self.company.id,
        })
        factor.action_approve()
        
        with self.assertRaises(ValidationError):
            factor.write({'kg_co2e_per_unit': 3.0})
        
        with self.assertRaises(ValidationError):
            factor.write({'code': 'DIESEL-TEST-V2'})
        
        with self.assertRaises(ValidationError):
            factor.write({'input_uom_id': self.uom_litre.id})

    def test_unique_code_version_company(self):
        """Test unique constraint on code, version, company"""
        self.env['ecodoo.emission.factor'].create({
            'name': 'Test Diesel',
            'code': 'DIESEL-TEST',
            'activity_type': 'fuel',
            'input_uom_id': self.uom_litre.id,
            'kg_co2e_per_unit': 2.5,
            'version': '1.0',
            'company_id': self.company.id,
        })
        with self.assertRaises(ValidationError):
            self.env['ecodoo.emission.factor'].create({
                'name': 'Test Diesel 2',
                'code': 'DIESEL-TEST',
                'activity_type': 'fuel',
                'input_uom_id': self.uom_litre.id,
                'kg_co2e_per_unit': 2.6,
                'version': '1.0',
                'company_id': self.company.id,
            })

    def test_positive_factor_constraint(self):
        """Test that kg_co2e_per_unit must be positive"""
        with self.assertRaises(ValidationError):
            self.env['ecodoo.emission.factor'].create({
                'name': 'Test',
                'code': 'TEST-NEG',
                'activity_type': 'fuel',
                'input_uom_id': self.uom_litre.id,
                'kg_co2e_per_unit': -1.0,
                'version': '1.0',
                'company_id': self.company.id,
            })


class TestCarbonTransaction(TransactionCase):
    """Test ecodoo.carbon.transaction model"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = cls.env.company
        cls.uom_litre = cls.env.ref('uom.product_uom_litre')
        cls.dept = cls.env['hr.department'].create({
            'name': 'Test Dept',
            'company_id': cls.company.id,
        })
        cls.factor = cls.env['ecodoo.emission.factor'].create({
            'name': 'Test Diesel',
            'code': 'DIESEL-TEST',
            'activity_type': 'fuel',
            'input_uom_id': cls.uom_litre.id,
            'kg_co2e_per_unit': 2.68,
            'version': '1.0',
            'state': 'approved',
            'valid_from': '2026-01-01',
            'valid_to': '2026-12-31',
            'company_id': cls.company.id,
        })

    def test_create_transaction_draft(self):
        """Test creating a draft transaction"""
        txn = self.env['ecodoo.carbon.transaction'].create({
            'name': 'TXN-001',
            'activity_date': '2026-07-12',
            'department_id': self.dept.id,
            'activity_type': 'fuel',
            'quantity': 100.0,
            'uom_id': self.uom_litre.id,
            'factor_id': self.factor.id,
            'company_id': self.company.id,
        })
        self.assertEqual(txn.state, 'draft')
        self.assertEqual(txn.kg_co2e, 0.0)

    def test_calculate_transaction(self):
        """Test calculating emissions"""
        txn = self.env['ecodoo.carbon.transaction'].create({
            'name': 'TXN-001',
            'activity_date': '2026-07-12',
            'department_id': self.dept.id,
            'activity_type': 'fuel',
            'quantity': 120.0,
            'uom_id': self.uom_litre.id,
            'factor_id': self.factor.id,
            'company_id': self.company.id,
        })
        txn.action_calculate()
        self.assertEqual(txn.state, 'calculated')
        self.assertEqual(txn.kg_co2e, 321.6)  # 120 * 2.68
        self.assertIn('321.600', txn.calculation_trace)

    def test_post_transaction(self):
        """Test posting a calculated transaction"""
        txn = self.env['ecodoo.carbon.transaction'].create({
            'name': 'TXN-001',
            'activity_date': '2026-07-12',
            'department_id': self.dept.id,
            'activity_type': 'fuel',
            'quantity': 120.0,
            'uom_id': self.uom_litre.id,
            'factor_id': self.factor.id,
            'company_id': self.company.id,
        })
        txn.action_calculate()
        txn.action_post()
        self.assertEqual(txn.state, 'posted')
        self.assertTrue(txn.posted_at)

    def test_posted_transaction_immutable(self):
        """Test that posted transactions cannot be modified"""
        txn = self.env['ecodoo.carbon.transaction'].create({
            'name': 'TXN-001',
            'activity_date': '2026-07-12',
            'department_id': self.dept.id,
            'activity_type': 'fuel',
            'quantity': 120.0,
            'uom_id': self.uom_litre.id,
            'factor_id': self.factor.id,
            'company_id': self.company.id,
        })
        txn.action_calculate()
        txn.action_post()
        
        with self.assertRaises(ValidationError):
            txn.write({'quantity': 200.0})
        
        with self.assertRaises(ValidationError):
            txn.write({'factor_id': self.factor.id})  # Same value but still triggers check

    def test_cancel_transaction(self):
        """Test cancelling a draft/calculated transaction"""
        txn = self.env['ecodoo.carbon.transaction'].create({
            'name': 'TXN-001',
            'activity_date': '2026-07-12',
            'department_id': self.dept.id,
            'activity_type': 'fuel',
            'quantity': 120.0,
            'uom_id': self.uom_litre.id,
            'factor_id': self.factor.id,
            'company_id': self.company.id,
        })
        txn.action_cancel()
        self.assertEqual(txn.state, 'cancelled')

    def test_cannot_cancel_posted(self):
        """Test that posted transactions cannot be cancelled"""
        txn = self.env['ecodoo.carbon.transaction'].create({
            'name': 'TXN-001',
            'activity_date': '2026-07-12',
            'department_id': self.dept.id,
            'activity_type': 'fuel',
            'quantity': 120.0,
            'uom_id': self.uom_litre.id,
            'factor_id': self.factor.id,
            'company_id': self.company.id,
        })
        txn.action_calculate()
        txn.action_post()
        
        with self.assertRaises(UserError):
            txn.action_cancel()

    def test_uom_conversion(self):
        """Test unit of measure conversion"""
        uom_ml = self.env['uom.uom'].create({
            'name': 'Milliliter',
            'category_id': self.uom_litre.category_id.id,
            'uom_type': 'smaller',
            'factor': 1000,
            'factor_inv': 0.001,
            'rounding': 0.001,
        })
        
        txn = self.env['ecodoo.carbon.transaction'].create({
            'name': 'TXN-002',
            'activity_date': '2026-07-12',
            'department_id': self.dept.id,
            'activity_type': 'fuel',
            'quantity': 120000.0,  # 120 L in mL
            'uom_id': uom_ml.id,
            'factor_id': self.factor.id,
            'company_id': self.company.id,
        })
        txn.action_calculate()
        self.assertEqual(txn.kg_co2e, 321.6)  # Should still be 120 L * 2.68


class TestGoal(TransactionCase):
    """Test ecodoo.goal model"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = cls.env.company
        cls.uom_litre = cls.env.ref('uom.product_uom_litre')
        cls.dept = cls.env['hr.department'].create({
            'name': 'Test Dept',
            'company_id': cls.company.id,
        })
        cls.factor = cls.env['ecodoo.emission.factor'].create({
            'name': 'Test Diesel',
            'code': 'DIESEL-TEST',
            'activity_type': 'fuel',
            'input_uom_id': cls.uom_litre.id,
            'kg_co2e_per_unit': 2.68,
            'version': '1.0',
            'state': 'approved',
            'valid_from': '2026-01-01',
            'valid_to': '2026-12-31',
            'company_id': cls.company.id,
        })

    def test_goal_creation(self):
        """Test creating a goal"""
        goal = self.env['ecodoo.goal'].create({
            'name': 'Test Goal',
            'department_id': self.dept.id,
            'period_start': '2026-07-01',
            'period_end': '2026-07-31',
            'target_kg_co2e': 300.0,
            'company_id': self.company.id,
        })
        self.assertEqual(goal.state, 'draft')
        self.assertEqual(goal.progress_percent, 0.0)
        self.assertEqual(goal.status, 'on_track')

    def test_goal_progress_calculation(self):
        """Test goal progress from posted transactions"""
        goal = self.env['ecodoo.goal'].create({
            'name': 'Test Goal',
            'department_id': self.dept.id,
            'period_start': '2026-07-01',
            'period_end': '2026-07-31',
            'target_kg_co2e': 300.0,
            'company_id': self.company.id,
        })
        # Create posted transaction
        txn = self.env['ecodoo.carbon.transaction'].create({
            'name': 'TXN-001',
            'activity_date': '2026-07-12',
            'department_id': self.dept.id,
            'activity_type': 'fuel',
            'quantity': 120.0,
            'uom_id': self.uom_litre.id,
            'factor_id': self.factor.id,
            'state': 'posted',
            'company_id': self.company.id,
        })
        goal.recompute_actuals()
        self.assertEqual(goal.actual_kg_co2e, 321.6)
        self.assertAlmostEqual(goal.progress_percent, 107.2, places=1)
        self.assertEqual(goal.status, 'at_risk')

    def test_goal_status_thresholds(self):
        """Test goal status thresholds"""
        goal = self.env['ecodoo.goal'].create({
            'name': 'Test Goal',
            'department_id': self.dept.id,
            'period_start': '2026-07-01',
            'period_end': '2026-07-31',
            'target_kg_co2e': 100.0,
            'company_id': self.company.id,
        })
        
        # On track: <= 100%
        goal.actual_kg_co2e = 80.0
        goal._compute_progress_percent()
        goal._compute_status()
        self.assertEqual(goal.status, 'on_track')
        
        # At risk: > 100% and <= 115%
        goal.actual_kg_co2e = 110.0
        goal._compute_progress_percent()
        goal._compute_status()
        self.assertEqual(goal.status, 'at_risk')
        
        # Off track: > 115%
        goal.actual_kg_co2e = 120.0
        goal._compute_progress_percent()
        goal._compute_status()
        self.assertEqual(goal.status, 'off_track')


class TestPolicy(TransactionCase):
    """Test ecodoo.policy and ecodoo.policy.acknowledgement models"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = cls.env.company
        cls.user = cls.env.user
        cls.emp = cls.env['hr.employee'].create({
            'name': 'Test Employee',
            'user_id': cls.user.id,
            'company_id': cls.company.id,
        })

    def test_policy_lifecycle(self):
        """Test policy state transitions"""
        policy = self.env['ecodoo.policy'].create({
            'name': 'Test Policy',
            'code': 'TEST-POL',
            'version': '1.0',
            'company_id': self.company.id,
        })
        self.assertEqual(policy.state, 'draft')
        
        policy.action_publish()
        self.assertEqual(policy.state, 'published')
        
        # Published policies are immutable
        with self.assertRaises(ValidationError):
            policy.write({'body': '<p>Changed</p>'})
        
        policy.action_archive()
        self.assertEqual(policy.state, 'archived')

    def test_acknowledgement_only_published(self):
        """Test that only published policies can be acknowledged"""
        policy = self.env['ecodoo.policy'].create({
            'name': 'Test Policy',
            'code': 'TEST-POL',
            'version': '1.0',
            'state': 'draft',
            'company_id': self.company.id,
        })
        
        with self.assertRaises(ValidationError):
            self.env['ecodoo.policy.acknowledgement'].create({
                'policy_id': policy.id,
                'employee_id': self.emp.id,
                'company_id': self.company.id,
            })
        
        policy.action_publish()
        ack = self.env['ecodoo.policy.acknowledgement'].create({
            'policy_id': policy.id,
            'employee_id': self.emp.id,
            'company_id': self.company.id,
        })
        self.assertEqual(ack.policy_id, policy)

    def test_unique_acknowledgement(self):
        """Test unique constraint on policy+employee"""
        policy = self.env['ecodoo.policy'].create({
            'name': 'Test Policy',
            'code': 'TEST-POL',
            'version': '1.0',
            'state': 'published',
            'company_id': self.company.id,
        })
        self.env['ecodoo.policy.acknowledgement'].create({
            'policy_id': policy.id,
            'employee_id': self.emp.id,
            'company_id': self.company.id,
        })
        with self.assertRaises(ValidationError):
            self.env['ecodoo.policy.acknowledgement'].create({
                'policy_id': policy.id,
                'employee_id': self.emp.id,
                'company_id': self.company.id,
            })


class TestComplianceIssue(TransactionCase):
    """Test ecodoo.compliance.issue model"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = cls.env.company
        cls.user = cls.env.user

    def test_issue_lifecycle(self):
        """Test issue state transitions"""
        issue = self.env['ecodoo.compliance.issue'].create({
            'name': 'Test Issue',
            'severity': 'medium',
            'owner_id': self.user.id,
            'company_id': self.company.id,
        })
        self.assertEqual(issue.state, 'open')
        
        issue.action_in_progress()
        self.assertEqual(issue.state, 'in_progress')
        
        with self.assertRaises(UserError):
            issue.action_resolve()  # Needs resolution
        
        issue.resolution = 'Fixed the issue'
        issue.action_resolve()
        self.assertEqual(issue.state, 'resolved')
        self.assertTrue(issue.resolved_at)
        
        issue.action_reopen()
        self.assertEqual(issue.state, 'open')
        self.assertFalse(issue.resolved_at)


class TestChallenge(TransactionCase):
    """Test ecodoo.challenge and participation models"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = cls.env.company
        cls.user_manager = cls.env.user
        cls.emp1 = cls.env['hr.employee'].create({
            'name': 'Emp 1',
            'user_id': cls.env['res.users'].create({'name': 'User1', 'login': 'u1@test.com'}).id,
            'company_id': cls.company.id,
        })
        cls.emp2 = cls.env['hr.employee'].create({
            'name': 'Emp 2',
            'user_id': cls.env['res.users'].create({'name': 'User2', 'login': 'u2@test.com'}).id,
            'company_id': cls.company.id,
        })

    def test_challenge_lifecycle(self):
        """Test challenge state transitions"""
        challenge = self.env['ecodoo.challenge'].create({
            'name': 'Test Challenge',
            'start_date': '2026-07-01',
            'end_date': '2026-07-31',
            'xp_reward': 50,
            'company_id': self.company.id,
        })
        self.assertEqual(challenge.state, 'draft')
        
        challenge.action_activate()
        self.assertEqual(challenge.state, 'active')
        
        challenge.action_close()
        self.assertEqual(challenge.state, 'closed')

    def test_participation_lifecycle(self):
        """Test participation state transitions and XP awarding"""
        challenge = self.env['ecodoo.challenge'].create({
            'name': 'Test Challenge',
            'start_date': '2026-07-01',
            'end_date': '2026-07-31',
            'xp_reward': 50,
            'state': 'active',
            'company_id': self.company.id,
        })
        
        part = self.env['ecodoo.challenge.participation'].create({
            'challenge_id': challenge.id,
            'employee_id': self.emp1.id,
            'company_id': self.company.id,
        })
        self.assertEqual(part.state, 'joined')
        
        with self.assertRaises(UserError):
            part.action_submit()  # Needs proof_note
        
        part.proof_note = 'Did the challenge'
        part.action_submit()
        self.assertEqual(part.state, 'submitted')
        
        part.action_approve()
        self.assertEqual(part.state, 'approved')
        self.assertTrue(part.xp_awarded)
        self.assertEqual(self.emp1.ecodoo_xp, 50)
        
        # Second approval should not double-award
        part.action_approve()
        self.assertEqual(self.emp1.ecodoo_xp, 50)

    def test_badge_award_on_approval(self):
        """Test badge is awarded when challenge has badge"""
        badge = self.env['ecodoo.badge'].create({
            'name': 'Test Badge',
            'xp_threshold': 50,
            'company_id': self.company.id,
        })
        challenge = self.env['ecodoo.challenge'].create({
            'name': 'Test Challenge',
            'start_date': '2026-07-01',
            'end_date': '2026-07-31',
            'xp_reward': 50,
            'badge_id': badge.id,
            'state': 'active',
            'company_id': self.company.id,
        })
        
        part = self.env['ecodoo.challenge.participation'].create({
            'challenge_id': challenge.id,
            'employee_id': self.emp1.id,
            'proof_note': 'Done',
            'company_id': self.company.id,
        })
        part.action_submit()
        part.action_approve()
        
        emp_badge = self.env['ecodoo.employee.badge'].search([
            ('employee_id', '=', self.emp1.id),
            ('badge_id', '=', badge.id),
        ])
        self.assertTrue(emp_badge)
        self.assertEqual(emp_badge.source_participation_id, part)

    def test_unique_participation(self):
        """Test unique challenge+employee constraint"""
        challenge = self.env['ecodoo.challenge'].create({
            'name': 'Test Challenge',
            'start_date': '2026-07-01',
            'end_date': '2026-07-31',
            'state': 'active',
            'company_id': self.company.id,
        })
        self.env['ecodoo.challenge.participation'].create({
            'challenge_id': challenge.id,
            'employee_id': self.emp1.id,
            'company_id': self.company.id,
        })
        with self.assertRaises(ValidationError):
            self.env['ecodoo.challenge.participation'].create({
                'challenge_id': challenge.id,
                'employee_id': self.emp1.id,
                'company_id': self.company.id,
            })


class TestDashboard(TransactionCase):
    """Test dashboard score calculations"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = cls.env.company
        cls.uom_litre = cls.env.ref('uom.product_uom_litre')
        cls.dept_logistics = cls.env['hr.department'].create({
            'name': 'Logistics',
            'company_id': cls.company.id,
        })
        cls.dept_ops = cls.env['hr.department'].create({
            'name': 'Operations',
            'company_id': cls.company.id,
        })
        cls.factor = cls.env['ecodoo.emission.factor'].create({
            'name': 'Diesel',
            'code': 'DIESEL',
            'activity_type': 'fuel',
            'input_uom_id': cls.uom_litre.id,
            'kg_co2e_per_unit': 2.68,
            'version': '1.0',
            'state': 'approved',
            'valid_from': '2026-01-01',
            'valid_to': '2026-12-31',
            'company_id': cls.company.id,
        })
        cls.user = cls.env.user
        cls.emp1 = cls.env['hr.employee'].create({
            'name': 'Emp 1',
            'user_id': cls.env['res.users'].create({'name': 'U1', 'login': 'u1@test.com'}).id,
            'department_id': cls.dept_logistics.id,
            'company_id': cls.company.id,
            'active': True,
        })
        cls.emp2 = cls.env['hr.employee'].create({
            'name': 'Emp 2',
            'user_id': cls.env['res.users'].create({'name': 'U2', 'login': 'u2@test.com'}).id,
            'department_id': cls.dept_logistics.id,
            'company_id': cls.company.id,
            'active': True,
        })
        cls.emp3 = cls.env['hr.employee'].create({
            'name': 'Emp 3',
            'user_id': cls.env['res.users'].create({'name': 'U3', 'login': 'u3@test.com'}).id,
            'department_id': cls.dept_ops.id,
            'company_id': cls.company.id,
            'active': True,
        })

    def test_environmental_score(self):
        """Test environmental score calculation"""
        # No active goals -> 0
        dashboard = self.env['ecodoo.dashboard']
        score = dashboard._compute_environmental_score(self.company)
        self.assertEqual(score, 0.0)
        
        # Create active goal with actual <= target
        goal = self.env['ecodoo.goal'].create({
            'name': 'Goal 1',
            'department_id': self.dept_logistics.id,
            'period_start': '2026-07-01',
            'period_end': '2026-07-31',
            'target_kg_co2e': 500.0,
            'state': 'active',
            'company_id': self.company.id,
        })
        txn = self.env['ecodoo.carbon.transaction'].create({
            'name': 'TXN-1',
            'activity_date': '2026-07-12',
            'department_id': self.dept_logistics.id,
            'activity_type': 'fuel',
            'quantity': 100.0,
            'uom_id': self.uom_litre.id,
            'factor_id': self.factor.id,
            'state': 'posted',
            'company_id': self.company.id,
        })
        score = dashboard._compute_environmental_score(self.company)
        self.assertEqual(score, 100.0)
        
        # actual > target
        txn2 = self.env['ecodoo.carbon.transaction'].create({
            'name': 'TXN-2',
            'activity_date': '2026-07-13',
            'department_id': self.dept_logistics.id,
            'activity_type': 'fuel',
            'quantity': 200.0,
            'uom_id': self.uom_litre.id,
            'factor_id': self.factor.id,
            'state': 'posted',
            'company_id': self.company.id,
        })
        goal.recompute_actuals()
        score = dashboard._compute_environmental_score(self.company)
        # target=500, actual=100*2.68+200*2.68=804, ratio=500/804*100=62.19
        self.assertAlmostEqual(score, 62.19, places=1)

    def test_social_score(self):
        """Test social score calculation"""
        dashboard = self.env['ecodoo.dashboard']
        score = dashboard._compute_social_score(self.company)
        self.assertEqual(score, 0.0)
        
        challenge = self.env['ecodoo.challenge'].create({
            'name': 'Challenge',
            'start_date': '2026-07-01',
            'end_date': '2026-07-31',
            'xp_reward': 50,
            'state': 'active',
            'company_id': self.company.id,
        })
        self.env['ecodoo.challenge.participation'].create({
            'challenge_id': challenge.id,
            'employee_id': self.emp1.id,
            'state': 'approved',
            'company_id': self.company.id,
        })
        self.env['ecodoo.challenge.participation'].create({
            'challenge_id': challenge.id,
            'employee_id': self.emp2.id,
            'state': 'approved',
            'company_id': self.company.id,
        })
        # 2 unique employees / 3 active employees * 100 = 66.67
        score = dashboard._compute_social_score(self.company)
        self.assertAlmostEqual(score, 66.67, places=1)

    def test_governance_score(self):
        """Test governance score calculation"""
        dashboard = self.env['ecodoo.dashboard']
        
        # No policies, no issues -> 0
        score = dashboard._compute_governance_score(self.company)
        self.assertEqual(score, 0.0)
        
        # Add published policy
        policy = self.env['ecodoo.policy'].create({
            'name': 'Policy 1',
            'code': 'POL1',
            'version': '1.0',
            'state': 'published',
            'company_id': self.company.id,
        })
        # 3 active employees, 1 policy
        self.env['ecodoo.policy.acknowledgement'].create({
            'policy_id': policy.id,
            'employee_id': self.emp1.id,
            'company_id': self.company.id,
        })
        self.env['ecodoo.policy.acknowledgement'].create({
            'policy_id': policy.id,
            'employee_id': self.emp2.id,
            'company_id': self.company.id,
        })
        # ack_rate = 2 / (1 * 3) = 0.667
        # No issues -> resolution_rate = 0
        # governance = 50 * 0.667 + 50 * 0 = 33.33
        score = dashboard._compute_governance_score(self.company)
        self.assertAlmostEqual(score, 33.33, places=1)
        
        # Add issues
        self.env['ecodoo.compliance.issue'].create({
            'name': 'Issue 1',
            'severity': 'low',
            'state': 'resolved',
            'resolved_at': '2026-07-01',
            'company_id': self.company.id,
        })
        self.env['ecodoo.compliance.issue'].create({
            'name': 'Issue 2',
            'severity': 'medium',
            'state': 'open',
            'company_id': self.company.id,
        })
        # resolution_rate = 1/2 = 0.5
        # governance = 50 * 0.667 + 50 * 0.5 = 33.33 + 25 = 58.33
        score = dashboard._compute_governance_score(self.company)
        self.assertAlmostEqual(score, 58.33, places=1)

    def test_overall_score(self):
        """Test overall score weights: 0.4*E + 0.3*S + 0.3*G"""
        dashboard = self.env['ecodoo.dashboard']
        # Set up E=100, S=50, G=50
        # overall = 0.4*100 + 0.3*50 + 0.3*50 = 40 + 15 + 15 = 70
        data = dashboard.get_dashboard_data()
        self.assertIn('overall_score', data)
        self.assertIn('score_disclaimer', data)