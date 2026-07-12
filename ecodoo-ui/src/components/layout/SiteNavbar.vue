<script setup lang="ts">
import PageContainer from './PageContainer.vue'
import BaseButton from '../ui/BaseButton.vue'
</script>
<template>
  <header class="absolute inset-x-0 top-0 z-20 pt-4 text-white">
    <PageContainer>
      <nav
        aria-label="Primary"
        class="flex min-h-16 flex-wrap items-center justify-between gap-x-5 rounded-xl border border-white/15 bg-navy/90 px-4 sm:px-6"
      >
        <RouterLink
          to="/"
          class="inline-flex min-h-11 items-center text-xl font-semibold text-white"
          >Ecodoo</RouterLink
        >
        <div
          class="order-3 flex w-full items-center gap-5 overflow-x-auto text-sm font-medium text-white/85 lg:order-none lg:w-auto lg:gap-6"
        >
          <a
            class="inline-flex min-h-11 shrink-0 items-center rounded-md px-1 hover:text-white"
            href="#platform"
            >Platform</a
          ><a
            class="inline-flex min-h-11 shrink-0 items-center rounded-md px-1 hover:text-white"
            href="#pillars"
            >ESG pillars</a
          >
          <a
            class="inline-flex min-h-11 shrink-0 items-center rounded-md px-1 hover:text-white"
            href="#traceability"
            >Evidence trail</a
          ><a
            class="inline-flex min-h-11 shrink-0 items-center rounded-md px-1 hover:text-white"
            href="#trust"
            >Trust</a
          >
        </div>
        <BaseButton href="/demo" size="compact">View demo</BaseButton>
      </nav>
    </PageContainer>
  </header>
</template>
