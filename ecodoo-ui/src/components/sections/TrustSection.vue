<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
import IconGlyph from '../ui/IconGlyph.vue'

const trustItems = [
  {
    title: 'Source lineage',
    desc: 'Drill from a reported result to its originating Odoo record in seconds.',
    icon: 'link',
  },
  {
    title: 'Controlled calculation',
    desc: 'See quantity, units, conversion path, factor version, and timestamp — always.',
    icon: 'settings',
  },
  {
    title: 'Review history',
    desc: 'Retain approval state and correction history without rewriting the past.',
    icon: 'clipboard',
  },
  {
    title: 'Odoo permissions',
    desc: 'Respect company boundaries and role-based access throughout the trace.',
    icon: 'lock',
  },
] as const
</script>

<template>
  <section id="trust" class="relative overflow-hidden bg-[#0a1628] py-24 sm:py-32">
    <!-- Decorative grid -->
    <div
      class="pointer-events-none absolute inset-0 opacity-[0.03]"
      aria-hidden="true"
      style="
        background-image:
          linear-gradient(rgba(255, 255, 255, 0.1) 1px, transparent 1px),
          linear-gradient(90deg, rgba(255, 255, 255, 0.1) 1px, transparent 1px);
        background-size: 60px 60px;
      "
    ></div>

    <!-- Glow -->
    <div
      class="pointer-events-none absolute right-0 top-1/2 h-[500px] w-[500px] -translate-y-1/2 rounded-full opacity-8"
      aria-hidden="true"
      style="background: radial-gradient(circle, #00c9b1 0%, transparent 65%)"
    ></div>

    <PageContainer class="relative">
      <div class="grid gap-16 lg:grid-cols-[1fr_1.2fr] lg:items-center">
        <!-- Left -->
        <div>
          <p class="mb-4 text-xs font-semibold uppercase tracking-widest text-teal">
            Trust by design
          </p>
          <h2 class="text-3xl font-bold text-white sm:text-5xl">Trust is visible in the record.</h2>
          <p class="mt-5 text-base leading-7 text-white/60">
            Ecodoo identifies estimates and provenance. It supports management and disclosure work —
            it does not claim legal, audit, or regulatory certification.
          </p>

          <!-- Disclaimer badge -->
          <div
            class="mt-8 inline-flex items-start gap-3 rounded-xl border border-yellow-500/20 bg-yellow-500/8 p-4 text-sm text-yellow-300/80"
          >
            <svg
              class="mt-0.5 h-5 w-5 shrink-0 text-yellow-400"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M8.485 2.495c.673-1.167 2.357-1.167 3.03 0l6.28 10.875c.673 1.167-.17 2.625-1.516 2.625H3.72c-1.347 0-2.189-1.458-1.515-2.625L8.485 2.495zM10 5a.75.75 0 01.75.75v3.5a.75.75 0 01-1.5 0v-3.5A.75.75 0 0110 5zm0 9a1 1 0 100-2 1 1 0 000 2z"
                clip-rule="evenodd"
              />
            </svg>
            Ecodoo reports identify estimates and data provenance. They do not constitute legal or
            regulatory certification.
          </div>
        </div>

        <!-- Right: Trust Items -->
        <div class="space-y-4">
          <div
            v-for="item in trustItems"
            :key="item.title"
            class="group flex gap-5 rounded-2xl border border-white/8 bg-white/5 p-6 backdrop-blur-sm transition-all duration-300 hover:border-teal/25 hover:bg-white/8"
          >
            <div
              class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl border border-white/10 bg-white/8 text-teal transition-all group-hover:border-teal/30 group-hover:bg-teal/10"
            >
              <IconGlyph :name="item.icon" class="h-5 w-5" />
            </div>
            <div>
              <h3 class="font-semibold text-white">{{ item.title }}</h3>
              <p class="mt-1.5 text-sm leading-6 text-white/55">{{ item.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </PageContainer>
  </section>
</template>
