<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
import SectionHeading from '../ui/SectionHeading.vue'
</script>
<template>
  <section id="platform" class="py-20 sm:py-28">
    <PageContainer>
      <div class="grid items-center gap-12 lg:grid-cols-[0.8fr_1.2fr]">
        <div>
          <SectionHeading
            title="ESG operations live where the work already happens"
            description="Fleet, purchase, expense, people, and governance records become one connected evidence model inside Odoo."
          />
          <dl class="mt-9 divide-y divide-navy/10 border-y border-navy/10">
            <div
              v-for="item in [
                ['Capture once', 'Approved operational records stay the source of truth.'],
                [
                  'Calculate transparently',
                  'Units, conversions, factors, and versions remain visible.',
                ],
                ['Act with context', 'Results connect directly to targets, issues, and reports.'],
              ]"
              :key="item[0]"
              class="grid gap-1 py-5 sm:grid-cols-[10rem_1fr]"
            >
              <dt class="font-semibold text-navy">{{ item[0] }}</dt>
              <dd class="text-muted">{{ item[1] }}</dd>
            </div>
          </dl>
        </div>
        <div class="overflow-hidden rounded-xl bg-mist">
          <div class="flex items-center justify-between bg-navy px-5 py-4 text-white">
            <div>
              <span class="font-semibold">Ecodoo</span
              ><span class="ml-4 text-sm text-white/70">Environmental ledger</span>
            </div>
            <span class="text-sm">Q2 2026</span>
          </div>
          <p class="bg-white px-5 py-2 text-xs font-semibold text-muted">Product preview</p>
          <div class="grid sm:grid-cols-[10rem_1fr]">
            <nav
              aria-label="Product preview"
              class="hidden border-r border-navy/10 p-5 text-sm sm:block"
            >
              <p class="font-semibold text-teal">Overview</p>
              <p class="mt-4 text-muted">Transactions</p>
              <p class="mt-4 text-muted">Factors</p>
              <p class="mt-4 text-muted">Goals</p>
              <p class="mt-4 text-muted">Reports</p>
            </nav>
            <div class="p-5 sm:p-7">
              <p class="text-sm text-muted">Evidence requiring review</p>
              <h3 class="mt-1 text-2xl font-semibold">Three records, one review path</h3>
              <div class="mt-7 divide-y divide-navy/10 border-y border-navy/10">
                <div
                  v-for="row in [
                    ['PO-2026-0418', 'Fleet fuel', 'Ready for review', 'text-teal'],
                    ['EXP-2026-0881', 'Rail travel', 'Factor needed', 'text-gold-ink'],
                    ['FLT-2026-0062', 'Vehicle distance', 'Approved', 'text-green-ink'],
                  ]"
                  :key="row[0]"
                  class="grid gap-2 py-4 text-sm sm:grid-cols-[1fr_1fr_auto]"
                >
                  <span class="font-mono text-navy">{{ row[0] }}</span
                  ><span>{{ row[1] }}</span
                  ><span :class="['font-medium', row[3]]">{{ row[2] }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </PageContainer>
  </section>
</template>
