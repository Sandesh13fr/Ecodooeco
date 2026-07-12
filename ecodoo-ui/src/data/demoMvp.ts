export type Role = 'employee' | 'manager' | 'executive'

export const roles: Role[] = ['employee', 'manager', 'executive']

export const navItems = [
  { page: 'command-center', label: 'Command Center', group: 'Overview' },
  { page: 'transactions', label: 'Carbon Transactions', group: 'Environment' },
  { page: 'factors', label: 'Emission Factors', group: 'Environment' },
  { page: 'goals', label: 'Sustainability Goals', group: 'Environment' },
  { page: 'challenges', label: 'Challenges', group: 'Social' },
  { page: 'participation', label: 'My Participation', group: 'Social' },
  { page: 'badges', label: 'My Badges', group: 'Social' },
  { page: 'policies', label: 'Policies', group: 'Governance' },
  { page: 'acknowledgements', label: 'Acknowledgements', group: 'Governance' },
  { page: 'issues', label: 'Compliance Issues', group: 'Governance' },
  { page: 'summary', label: 'ESG Summary', group: 'Reporting' },
] as const

export type PageKey = (typeof navItems)[number]['page']

export const demoData = {
  company: 'GreenRoute Logistics Pvt Ltd',
  generatedAt: '2026-07-12T16:30:00Z',
  scoreDisclaimer: 'Demonstration management score; not a reporting standard or assurance result.',
  limitation:
    'Supports internal ESG management and demonstration only; not independent assurance, certification, or proof of regulatory compliance.',
  scores: {
    environmental: 93.28,
    social: 50,
    governance: 62.5,
    overall: 71.06,
  },
  factor: {
    code: 'DIESEL-DEMO',
    name: 'Demo diesel emission factor',
    version: '1.0',
    activityType: 'Fuel',
    factor: 2.68,
    unit: 'kg CO2e/L',
    validity: '2026-01-01 to 2026-12-31',
    state: 'approved',
    source: 'Synthetic hackathon fixture; replace with approved factor source before use.',
  },
  transaction: {
    id: 1,
    name: 'Logistics diesel',
    activityDate: '2026-07-12',
    department: 'Logistics',
    activityType: 'Fleet fuel',
    sourceReference: 'PO-2026-0418',
    quantity: '120.000',
    unit: 'L',
    factorCode: 'DIESEL-DEMO v1.0',
    kgCo2e: 321.6,
    trace: '120.000 L x 2.680000 kg CO2e/L = 321.600 kg CO2e',
    state: 'calculated',
    calculatedAt: '2026-07-12T16:30:00Z',
    postedAt: 'Not posted',
  },
  goal: {
    department: 'Logistics',
    period: 'July 2026',
    targetKgCo2e: 300,
    actualKgCo2e: 321.6,
    status: 'at_risk',
  },
  governance: {
    policy: 'Sustainable Operations Policy v1.0',
    acknowledgementStatus: '3 of 4 employees',
    acknowledgementAction: 'Acknowledge policy',
    issues: [
      {
        title: 'Missing supplier fuel evidence',
        severity: 'High',
        owner: 'Finance',
        dueDate: '2026-07-18',
        state: 'Open',
        resolution: 'Awaiting supplier invoice attachment',
      },
      {
        title: 'Quarterly policy review',
        severity: 'Medium',
        owner: 'Operations',
        dueDate: '2026-07-10',
        state: 'Resolved',
        resolution: 'Reviewed and attached to policy record',
      },
    ],
  },
  social: {
    challenge: 'Car-Free Commute',
    dates: '01 Jul-31 Jul 2026',
    xp: 50,
    approvedParticipations: 2,
    proof: 'Two approved commute logs',
    badge: 'Eco Starter',
    employeeCount: 4,
  },
  departments: [{ department: 'Logistics', kgCo2e: 321.6 }],
}

export const goalProgress = (demoData.goal.actualKgCo2e / demoData.goal.targetKgCo2e) * 100
