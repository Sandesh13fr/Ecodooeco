<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import PageContainer from '../components/layout/PageContainer.vue'
import BaseButton from '../components/ui/BaseButton.vue'
import { demoData, goalProgress, navItems, roles, type PageKey, type Role } from '../data/demoMvp'

const route = useRoute()
const pageKeys = navItems.map((item) => item.page)

const currentPage = computed<PageKey>(() => {
  const page = route.params.page
  return pageKeys.includes(page as PageKey) ? (page as PageKey) : 'command-center'
})

const role = computed<Role>(() => {
  const raw = route.query.role
  return roles.includes(raw as Role) ? (raw as Role) : 'manager'
})

const currentNav = computed(
  () => navItems.find((item) => item.page === currentPage.value) ?? navItems[0],
)
const progressWidth = computed(() => `${Math.min(goalProgress, 100).toFixed(1)}%`)
const canManage = computed(() => role.value === 'manager')

function routeFor(page: PageKey, selectedRole = role.value) {
  return { path: `/app/${page}`, query: { role: selectedRole } }
}

function statusClass(status: string) {
  if (['approved', 'calculated', 'Resolved'].includes(status)) return 'bg-green/15 text-green-ink'
  if (['at_risk', 'Open', 'High'].includes(status)) return 'bg-gold/20 text-gold-ink'
  return 'bg-mist text-muted'
}

function printSummary() {
  window.print()
}
</script>

<template>
  <main class="min-h-screen bg-mist text-ink">
    <PageContainer class="py-6 sm:py-8">
      <header class="no-print flex flex-wrap items-center justify-between gap-4">
        <RouterLink
          to="/"
          class="inline-flex min-h-11 items-center text-xl font-semibold text-navy"
        >
          Ecodoo
        </RouterLink>
        <div class="flex flex-wrap items-center gap-2" aria-label="Presentation role">
          <RouterLink
            v-for="item in roles"
            :key="item"
            :to="routeFor(currentPage, item)"
            :class="[
              'inline-flex min-h-11 items-center rounded-lg px-3 text-sm font-semibold capitalize',
              role === item ? 'bg-navy text-white' : 'border border-navy/15 bg-white text-navy',
            ]"
          >
            {{ item }}
          </RouterLink>
        </div>
      </header>

      <div class="mt-6 grid gap-6 lg:grid-cols-[17rem_1fr]">
        <aside class="no-print rounded-xl bg-white p-3">
          <p class="px-3 py-2 text-sm font-semibold text-muted">Demo navigation</p>
          <nav class="grid gap-1" aria-label="MVP demo">
            <RouterLink
              v-for="item in navItems"
              :key="item.page"
              :to="routeFor(item.page)"
              :class="[
                'rounded-lg px-3 py-2 text-sm font-medium',
                currentPage === item.page ? 'bg-teal text-white' : 'text-ink hover:bg-mist',
              ]"
            >
              <span class="block text-xs opacity-75">{{ item.group }}</span>
              {{ item.label }}
            </RouterLink>
          </nav>
        </aside>

        <section class="min-w-0">
          <div class="print-page rounded-xl bg-white p-5 sm:p-8">
            <div
              class="mb-8 flex flex-col justify-between gap-4 border-b border-navy/10 pb-6 md:flex-row"
            >
              <div>
                <p class="text-sm font-semibold text-teal">{{ demoData.company }}</p>
                <h1 class="mt-2 text-3xl font-semibold text-navy sm:text-4xl">
                  {{ currentNav.label }}
                </h1>
                <p class="mt-3 max-w-[70ch] leading-7 text-muted">
                  Demo fallback data is active. Live backend integration can map into this contract
                  without changing the visible workflow.
                </p>
              </div>
              <div class="text-sm text-muted">
                <p class="font-semibold capitalize text-navy">{{ role }} view</p>
                <p class="mt-1 font-mono">{{ demoData.generatedAt }}</p>
              </div>
            </div>

            <template v-if="currentPage === 'command-center'">
              <div class="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
                <article
                  v-for="item in [
                    ['Overall score', demoData.scores.overall],
                    ['Environmental', demoData.scores.environmental],
                    ['Social', demoData.scores.social],
                    ['Governance', demoData.scores.governance],
                  ]"
                  :key="item[0]"
                  class="rounded-xl border border-navy/10 p-5"
                >
                  <p class="text-sm text-muted">{{ item[0] }}</p>
                  <p class="mt-2 font-mono text-3xl font-semibold tabular-nums text-navy">
                    {{ item[1] }}
                  </p>
                </article>
              </div>

              <p class="mt-4 rounded-lg bg-mist p-4 text-sm font-medium text-navy">
                {{ demoData.scoreDisclaimer }}
              </p>

              <div class="mt-8 grid gap-5 lg:grid-cols-[1.1fr_0.9fr]">
                <article class="rounded-xl border border-navy/10 p-5">
                  <h2 class="text-xl font-semibold text-navy">Department emissions</h2>
                  <div class="mt-5 space-y-4">
                    <div v-for="dept in demoData.departments" :key="dept.department">
                      <div class="flex justify-between gap-4 text-sm">
                        <span class="font-medium">{{ dept.department }}</span>
                        <span class="font-mono tabular-nums">{{ dept.kgCo2e }} kg CO2e</span>
                      </div>
                      <div class="mt-2 h-3 overflow-hidden rounded-full bg-mist">
                        <div class="h-full rounded-full bg-teal" style="width: 100%"></div>
                      </div>
                    </div>
                  </div>
                </article>

                <article class="rounded-xl border border-navy/10 p-5">
                  <h2 class="text-xl font-semibold text-navy">Fallback states</h2>
                  <ul class="mt-4 space-y-3 text-sm text-muted">
                    <li>Loading: show skeleton cards while dashboard data is requested.</li>
                    <li>Empty: point users to Carbon Transactions.</li>
                    <li>Error: keep this fixture visible and link to the trace record.</li>
                  </ul>
                  <div class="mt-5">
                    <BaseButton href="/app/transactions" size="compact"
                      >Carbon Transactions</BaseButton
                    >
                  </div>
                </article>
              </div>
            </template>

            <template v-else-if="currentPage === 'transactions'">
              <div class="grid gap-6 xl:grid-cols-[0.8fr_1.2fr]">
                <article class="rounded-xl border border-navy/10 p-5">
                  <h2 class="text-xl font-semibold text-navy">{{ demoData.transaction.name }}</h2>
                  <dl class="mt-5 divide-y divide-navy/10 text-sm">
                    <div
                      v-for="item in [
                        ['Activity date', demoData.transaction.activityDate],
                        ['Department', demoData.transaction.department],
                        ['Activity type', demoData.transaction.activityType],
                        ['Source reference', demoData.transaction.sourceReference],
                        ['State', demoData.transaction.state],
                      ]"
                      :key="item[0]"
                      class="grid gap-2 py-3 sm:grid-cols-[10rem_1fr]"
                    >
                      <dt class="font-semibold text-navy">{{ item[0] }}</dt>
                      <dd class="text-muted">{{ item[1] }}</dd>
                    </div>
                  </dl>
                  <div v-if="canManage" class="mt-5 flex flex-wrap gap-2">
                    <button
                      class="min-h-11 rounded-lg bg-teal px-4 text-sm font-semibold text-white"
                    >
                      Calculate
                    </button>
                    <button
                      class="min-h-11 rounded-lg border border-navy/20 px-4 text-sm font-semibold text-navy"
                    >
                      Post
                    </button>
                    <button
                      class="min-h-11 rounded-lg border border-danger/40 px-4 text-sm font-semibold text-danger"
                    >
                      Cancel
                    </button>
                  </div>
                  <p v-else class="mt-5 rounded-lg bg-mist p-3 text-sm text-muted">
                    Actions hidden in {{ role }} view. Server permissions remain authoritative.
                  </p>
                </article>

                <article class="rounded-xl bg-navy p-5 text-white">
                  <p class="text-sm font-semibold text-teal-light">Read-only calculation trace</p>
                  <p class="mt-4 font-mono text-2xl font-semibold tabular-nums">
                    {{ demoData.transaction.kgCo2e }} kg CO2e
                  </p>
                  <code class="mt-5 block rounded-lg bg-white/10 p-4 text-sm leading-6 text-white">
                    {{ demoData.transaction.trace }}
                  </code>
                  <dl class="mt-5 grid gap-4 text-sm sm:grid-cols-2">
                    <div>
                      <dt class="text-white/70">Quantity</dt>
                      <dd class="font-mono">
                        {{ demoData.transaction.quantity }} {{ demoData.transaction.unit }}
                      </dd>
                    </div>
                    <div>
                      <dt class="text-white/70">Factor</dt>
                      <dd class="font-mono">{{ demoData.transaction.factorCode }}</dd>
                    </div>
                    <div>
                      <dt class="text-white/70">Calculated</dt>
                      <dd class="font-mono">{{ demoData.transaction.calculatedAt }}</dd>
                    </div>
                    <div>
                      <dt class="text-white/70">Posted</dt>
                      <dd class="font-mono">{{ demoData.transaction.postedAt }}</dd>
                    </div>
                  </dl>
                </article>
              </div>
            </template>

            <template v-else-if="currentPage === 'factors'">
              <article class="rounded-xl border border-navy/10 p-5">
                <div class="flex flex-wrap justify-between gap-4">
                  <div>
                    <h2 class="text-xl font-semibold text-navy">{{ demoData.factor.name }}</h2>
                    <p class="mt-1 font-mono text-sm text-muted">
                      {{ demoData.factor.code }} · v{{ demoData.factor.version }}
                    </p>
                  </div>
                  <span
                    :class="[
                      'rounded-full px-3 py-1 text-sm font-semibold',
                      statusClass(demoData.factor.state),
                    ]"
                  >
                    {{ demoData.factor.state }}
                  </span>
                </div>
                <dl class="mt-5 grid gap-4 text-sm sm:grid-cols-2">
                  <div>
                    <dt class="font-semibold text-navy">Activity type</dt>
                    <dd class="mt-1 text-muted">{{ demoData.factor.activityType }}</dd>
                  </div>
                  <div>
                    <dt class="font-semibold text-navy">Factor</dt>
                    <dd class="mt-1 font-mono text-muted">
                      {{ demoData.factor.factor }} {{ demoData.factor.unit }}
                    </dd>
                  </div>
                  <div>
                    <dt class="font-semibold text-navy">Validity</dt>
                    <dd class="mt-1 text-muted">{{ demoData.factor.validity }}</dd>
                  </div>
                  <div>
                    <dt class="font-semibold text-navy">Provenance</dt>
                    <dd class="mt-1 text-muted">{{ demoData.factor.source }}</dd>
                  </div>
                </dl>
              </article>
            </template>

            <template v-else-if="currentPage === 'goals'">
              <article class="rounded-xl border border-navy/10 p-5">
                <div class="flex flex-wrap justify-between gap-4">
                  <div>
                    <h2 class="text-xl font-semibold text-navy">
                      {{ demoData.goal.department }} intensity · {{ demoData.goal.period }}
                    </h2>
                    <p class="mt-1 text-muted">
                      Target vs actual emissions from posted/calculated data.
                    </p>
                  </div>
                  <span
                    :class="[
                      'rounded-full px-3 py-1 text-sm font-semibold',
                      statusClass(demoData.goal.status),
                    ]"
                  >
                    At risk
                  </span>
                </div>
                <div class="mt-6">
                  <div class="flex justify-between gap-4 text-sm">
                    <span>{{ goalProgress.toFixed(1) }}% of target used</span>
                    <span class="font-mono tabular-nums">
                      {{ demoData.goal.actualKgCo2e }} / {{ demoData.goal.targetKgCo2e }} kg CO2e
                    </span>
                  </div>
                  <div class="mt-2 h-4 overflow-hidden rounded-full bg-mist">
                    <div
                      class="h-full rounded-full bg-gold"
                      :style="{ width: progressWidth }"
                    ></div>
                  </div>
                </div>
              </article>
            </template>

            <template v-else-if="currentPage === 'challenges'">
              <article class="rounded-xl border border-navy/10 p-5">
                <p class="text-sm font-semibold text-cobalt">Active challenge</p>
                <h2 class="mt-2 text-2xl font-semibold text-navy">
                  {{ demoData.social.challenge }}
                </h2>
                <p class="mt-3 text-muted">
                  {{ demoData.social.dates }} · {{ demoData.social.xp }} XP reward
                </p>
                <p class="mt-4 text-sm text-muted">
                  {{ demoData.social.approvedParticipations }} approved participations. Employee
                  participation is opt-in and shown as aggregate demo data here.
                </p>
              </article>
            </template>

            <template v-else-if="currentPage === 'participation'">
              <article class="rounded-xl border border-navy/10 p-5">
                <h2 class="text-xl font-semibold text-navy">My participation</h2>
                <p class="mt-3 text-muted">{{ demoData.social.proof }}</p>
                <p class="mt-4 rounded-lg bg-mist p-3 text-sm text-muted">
                  Manager view can approve or reject participation. Employee view sees own status
                  only.
                </p>
              </article>
            </template>

            <template v-else-if="currentPage === 'badges'">
              <article class="rounded-xl border border-navy/10 p-5">
                <p class="text-sm font-semibold text-cobalt">My badges</p>
                <h2 class="mt-2 text-2xl font-semibold text-navy">{{ demoData.social.badge }}</h2>
                <p class="mt-3 font-mono text-muted">{{ demoData.social.xp }} XP earned</p>
              </article>
            </template>

            <template v-else-if="currentPage === 'policies'">
              <article class="rounded-xl border border-navy/10 p-5">
                <p class="text-sm font-semibold text-gold-ink">Published policy</p>
                <h2 class="mt-2 text-2xl font-semibold text-navy">
                  {{ demoData.governance.policy }}
                </h2>
                <p class="mt-3 text-muted">
                  Owner: Operations · Effective: 2026-07-01 · Review: 2026-10-01
                </p>
                <p class="mt-4 max-w-[70ch] leading-7 text-muted">
                  Employees acknowledge operating guidance for fuel evidence, commute participation,
                  supplier records, and corrective action ownership.
                </p>
              </article>
            </template>

            <template v-else-if="currentPage === 'acknowledgements'">
              <article class="rounded-xl border border-navy/10 p-5">
                <h2 class="text-xl font-semibold text-navy">Policy acknowledgements</h2>
                <p class="mt-3 text-muted">
                  {{ demoData.governance.acknowledgementStatus }} acknowledged.
                </p>
                <button
                  class="mt-5 min-h-11 rounded-lg bg-teal px-4 text-sm font-semibold text-white"
                >
                  {{ demoData.governance.acknowledgementAction }}
                </button>
              </article>
            </template>

            <template v-else-if="currentPage === 'issues'">
              <div class="grid gap-4">
                <article
                  v-for="issue in demoData.governance.issues"
                  :key="issue.title"
                  class="rounded-xl border border-navy/10 p-5"
                >
                  <div class="flex flex-wrap justify-between gap-3">
                    <h2 class="text-xl font-semibold text-navy">{{ issue.title }}</h2>
                    <span
                      :class="[
                        'rounded-full px-3 py-1 text-sm font-semibold',
                        statusClass(issue.state),
                      ]"
                    >
                      {{ issue.severity }} · {{ issue.state }}
                    </span>
                  </div>
                  <p class="mt-3 text-muted">
                    Owner: {{ issue.owner }} · Due: {{ issue.dueDate }} · {{ issue.resolution }}
                  </p>
                </article>
              </div>
            </template>

            <template v-else>
              <article>
                <div class="flex flex-wrap justify-between gap-4">
                  <div>
                    <p class="text-sm font-semibold text-teal">One-page ESG Summary</p>
                    <h2 class="mt-2 text-2xl font-semibold text-navy">{{ demoData.company }}</h2>
                    <p class="mt-1 text-muted">Reporting date: 2026-07-12</p>
                  </div>
                  <button
                    class="no-print min-h-11 rounded-lg bg-teal px-4 text-sm font-semibold text-white"
                    @click="printSummary"
                  >
                    Print summary
                  </button>
                </div>

                <div class="mt-6 grid gap-4 sm:grid-cols-4">
                  <div
                    v-for="item in [
                      ['Overall', demoData.scores.overall],
                      ['E', demoData.scores.environmental],
                      ['S', demoData.scores.social],
                      ['G', demoData.scores.governance],
                    ]"
                    :key="item[0]"
                    class="rounded-lg border border-navy/10 p-4"
                  >
                    <p class="text-sm text-muted">{{ item[0] }}</p>
                    <p class="mt-1 font-mono text-2xl font-semibold tabular-nums text-navy">
                      {{ item[1] }}
                    </p>
                  </div>
                </div>

                <dl class="mt-6 grid gap-4 text-sm md:grid-cols-2">
                  <div class="rounded-lg bg-mist p-4">
                    <dt class="font-semibold text-navy">Environmental</dt>
                    <dd class="mt-2 text-muted">
                      {{ demoData.transaction.trace }} using {{ demoData.factor.code }} v{{
                        demoData.factor.version
                      }}.
                    </dd>
                  </div>
                  <div class="rounded-lg bg-mist p-4">
                    <dt class="font-semibold text-navy">Social</dt>
                    <dd class="mt-2 text-muted">
                      {{ demoData.social.approvedParticipations }} approved participations,
                      {{ demoData.social.badge }} badge, {{ demoData.social.xp }} XP.
                    </dd>
                  </div>
                  <div class="rounded-lg bg-mist p-4">
                    <dt class="font-semibold text-navy">Governance</dt>
                    <dd class="mt-2 text-muted">
                      {{ demoData.governance.acknowledgementStatus }} acknowledgements; 1 open and 1
                      resolved issue.
                    </dd>
                  </div>
                  <div class="rounded-lg bg-mist p-4">
                    <dt class="font-semibold text-navy">Limitations</dt>
                    <dd class="mt-2 text-muted">{{ demoData.limitation }}</dd>
                  </div>
                </dl>
              </article>
            </template>
          </div>
        </section>
      </div>
    </PageContainer>
  </main>
</template>
