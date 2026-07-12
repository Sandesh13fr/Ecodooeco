<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'

const pillars = [
  {
    key: 'E',
    label: 'Environmental',
    headline: 'Measure operational impact.',
    desc: 'Build emissions ledgers from activity data, controlled factors, and explicit calculation units.',
    color: 'teal',
    accentBg: 'rgba(0,201,177,0.08)',
    accentBorder: 'rgba(0,201,177,0.25)',
    accentText: '#00c9b1',
    accentGlow: 'rgba(0,201,177,0.15)',
    items: ['Scope 1, 2 & 3 emissions', 'Versioned emission factors', 'Carbon transaction ledger'],
  },
  {
    key: 'S',
    label: 'Social',
    headline: 'See progress without exposing people.',
    desc: 'Track aggregate workforce measures with role-aware access controls and privacy boundaries.',
    color: 'cobalt',
    accentBg: 'rgba(59,130,246,0.08)',
    accentBorder: 'rgba(59,130,246,0.25)',
    accentText: '#60a5fa',
    accentGlow: 'rgba(59,130,246,0.15)',
    items: ['Workforce diversity metrics', 'Health & safety tracking', 'Community engagement'],
  },
  {
    key: 'G',
    label: 'Governance',
    headline: 'Turn policy into accountable action.',
    desc: 'Manage policies, acknowledgements, audits, and issue closure — fully in context of operations.',
    color: 'gold',
    accentBg: 'rgba(245,158,11,0.08)',
    accentBorder: 'rgba(245,158,11,0.25)',
    accentText: '#fbbf24',
    accentGlow: 'rgba(245,158,11,0.15)',
    items: ['Policy acknowledgements', 'Risk & compliance tracking', 'Ethics transparency'],
  },
]
</script>

<template>
  <section id="pillars" class="relative overflow-hidden bg-white py-24 sm:py-32">
    <!-- Subtle background -->
    <div class="pointer-events-none absolute inset-0" aria-hidden="true">
      <div class="absolute inset-0" style="background: linear-gradient(180deg, #f0faf8 0%, #ffffff 40%)"></div>
    </div>

    <PageContainer class="relative">
      <!-- Header -->
      <div class="mx-auto max-w-2xl text-center">
        <p class="mb-4 text-xs font-semibold uppercase tracking-widest text-teal">ESG Pillars</p>
        <h2 class="text-3xl font-bold text-[#0a1628] sm:text-5xl">
          Three disciplines. One accountable operating model.
        </h2>
        <p class="mt-5 text-base leading-7 text-[#64748b]">
          Environmental impact, social responsibility, and governance integrity — all connected
          through a single Odoo-native evidence trail.
        </p>
      </div>

      <!-- Pillar Cards -->
      <div class="mt-16 grid gap-6 lg:grid-cols-3">
        <article
          v-for="(pillar, i) in pillars"
          :key="pillar.key"
          class="group relative overflow-hidden rounded-2xl border p-8 transition-all duration-500 hover:-translate-y-2 hover:shadow-2xl"
          :style="{
            borderColor: pillar.accentBorder,
            background: `linear-gradient(145deg, ${pillar.accentBg}, rgba(255,255,255,0.5))`,
            transitionDelay: `${i * 60}ms`,
          }"
        >
          <!-- Glow on hover -->
          <div
            class="pointer-events-none absolute inset-0 rounded-2xl opacity-0 transition-opacity duration-500 group-hover:opacity-100"
            :style="{ boxShadow: `0 0 50px ${pillar.accentGlow}, inset 0 1px 0 rgba(255,255,255,0.3)` }"
          ></div>

          <!-- Letter Badge -->
          <div
            class="relative mb-6 inline-flex h-12 w-12 items-center justify-center rounded-xl text-xl font-black"
            :style="{ background: pillar.accentBg, border: `1px solid ${pillar.accentBorder}`, color: pillar.accentText }"
          >
            {{ pillar.key }}
          </div>

          <!-- Content -->
          <p class="relative text-xs font-bold uppercase tracking-widest" :style="{ color: pillar.accentText }">
            {{ pillar.label }}
          </p>
          <h3 class="relative mt-3 text-xl font-bold text-[#0a1628]">{{ pillar.headline }}</h3>
          <p class="relative mt-3 text-sm leading-6 text-[#64748b]">{{ pillar.desc }}</p>

          <!-- Feature List -->
          <ul class="relative mt-6 space-y-2">
            <li
              v-for="item in pillar.items"
              :key="item"
              class="flex items-center gap-2.5 text-sm text-[#475569]"
            >
              <svg class="h-4 w-4 shrink-0" :style="{ color: pillar.accentText }" viewBox="0 0 16 16" fill="none">
                <path d="M3 8l3.5 3.5L13 4.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              {{ item }}
            </li>
          </ul>
        </article>
      </div>

      <!-- Bottom connector -->
      <div class="mt-16 flex items-center justify-center gap-4">
        <div class="h-px flex-1" style="background: linear-gradient(to right, transparent, rgba(0,201,177,0.3))"></div>
        <span class="text-sm font-medium text-[#64748b]">All connected in one Odoo add-on suite</span>
        <div class="h-px flex-1" style="background: linear-gradient(to left, transparent, rgba(0,201,177,0.3))"></div>
      </div>
    </PageContainer>
  </section>
</template>
