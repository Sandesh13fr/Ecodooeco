<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
</script>

<template>
  <section id="platform" class="relative overflow-hidden bg-[#0a1628] py-24 sm:py-32">
    <!-- Background mesh -->
    <div class="pointer-events-none absolute inset-0" aria-hidden="true">
      <div
        class="absolute -top-40 left-1/4 h-[500px] w-[500px] rounded-full opacity-10"
        style="background: radial-gradient(circle, #00c9b1 0%, transparent 70%)"
      ></div>
      <div
        class="absolute bottom-0 right-0 h-[400px] w-[400px] rounded-full opacity-8"
        style="background: radial-gradient(circle, #3b82f6 0%, transparent 70%)"
      ></div>
    </div>

    <PageContainer class="relative">
      <!-- Section label -->
      <p class="mb-4 text-xs font-semibold uppercase tracking-widest text-teal">Platform</p>

      <div class="grid items-start gap-16 lg:grid-cols-[1fr_1.2fr]">
        <!-- Left: Text -->
        <div>
          <h2 class="text-3xl font-bold leading-tight text-white sm:text-4xl lg:text-5xl">
            ESG operations live where the work already happens
          </h2>
          <p class="mt-5 text-base leading-7 text-white/60">
            Fleet, purchase, expense, people, and governance records become one connected
            evidence model — inside Odoo, without a parallel database.
          </p>

          <dl class="mt-10 space-y-0 divide-y divide-white/8">
            <div
              v-for="item in [
                { label: 'Capture once', desc: 'Approved operational records stay the source of truth.', icon: '→' },
                { label: 'Calculate transparently', desc: 'Units, conversions, factors, and versions remain visible.', icon: '÷' },
                { label: 'Act with context', desc: 'Results connect directly to targets, issues, and reports.', icon: '↗' },
              ]"
              :key="item.label"
              class="group flex gap-5 py-5 transition-all duration-300 hover:border-teal/20"
            >
              <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-lg border border-teal/20 bg-teal/8 text-base font-bold text-teal transition-all group-hover:border-teal/40 group-hover:bg-teal/15">
                {{ item.icon }}
              </div>
              <div>
                <dt class="font-semibold text-white">{{ item.label }}</dt>
                <dd class="mt-1 text-sm leading-6 text-white/55">{{ item.desc }}</dd>
              </div>
            </div>
          </dl>
        </div>

        <!-- Right: Product Preview Card -->
        <div class="overflow-hidden rounded-2xl border border-white/10 bg-white/5 shadow-[0_24px_80px_rgba(0,0,0,0.4)] backdrop-blur-sm card-hover">
          <!-- Card Header -->
          <div class="flex items-center justify-between border-b border-white/8 bg-white/5 px-6 py-4">
            <div class="flex items-center gap-3">
              <div class="flex gap-1.5">
                <div class="h-3 w-3 rounded-full bg-red-500/80"></div>
                <div class="h-3 w-3 rounded-full bg-yellow-500/80"></div>
                <div class="h-3 w-3 rounded-full bg-green-500/80"></div>
              </div>
              <span class="text-sm font-semibold text-white">Ecodoo · Environmental Ledger</span>
            </div>
            <span class="rounded-full border border-teal/30 bg-teal/10 px-2.5 py-0.5 text-xs font-medium text-teal">Q2 2026</span>
          </div>

          <!-- Card Body -->
          <div class="grid sm:grid-cols-[9rem_1fr]">
            <!-- Sidebar -->
            <nav class="hidden border-r border-white/8 p-5 text-sm sm:block">
              <p class="font-semibold text-teal">Overview</p>
              <p class="mt-4 text-white/40">Transactions</p>
              <p class="mt-4 text-white/40">Factors</p>
              <p class="mt-4 text-white/40">Goals</p>
              <p class="mt-4 text-white/40">Reports</p>
            </nav>

            <!-- Main Content -->
            <div class="p-6">
              <p class="text-xs font-medium text-white/50">Evidence requiring review</p>
              <h3 class="mt-1 text-lg font-semibold text-white">Three records, one review path</h3>

              <div class="mt-6 space-y-0 divide-y divide-white/8">
                <div
                  v-for="row in [
                    { id: 'PO-2026-0418', category: 'Fleet fuel', status: 'Ready for review', color: 'text-teal', dot: 'bg-teal' },
                    { id: 'EXP-2026-0881', category: 'Rail travel', status: 'Factor needed', color: 'text-yellow-400', dot: 'bg-yellow-400' },
                    { id: 'FLT-2026-0062', category: 'Vehicle distance', status: 'Approved', color: 'text-green-400', dot: 'bg-green-400' },
                  ]"
                  :key="row.id"
                  class="flex items-center justify-between gap-4 py-3.5 text-sm"
                >
                  <span class="font-mono text-white/80">{{ row.id }}</span>
                  <span class="hidden text-white/55 sm:block">{{ row.category }}</span>
                  <span :class="['flex items-center gap-1.5 font-medium', row.color]">
                    <span :class="['h-1.5 w-1.5 rounded-full', row.dot]"></span>
                    {{ row.status }}
                  </span>
                </div>
              </div>

              <!-- Mini stats -->
              <div class="mt-6 grid grid-cols-3 gap-3">
                <div
                  v-for="stat in [
                    { val: '1,732', label: 'tCO₂e' },
                    { val: '73%', label: 'On track' },
                    { val: '23', label: 'Open actions' },
                  ]"
                  :key="stat.label"
                  class="rounded-xl border border-white/8 bg-white/5 p-3 text-center"
                >
                  <p class="text-lg font-bold text-teal">{{ stat.val }}</p>
                  <p class="mt-0.5 text-xs text-white/45">{{ stat.label }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </PageContainer>
  </section>
</template>
