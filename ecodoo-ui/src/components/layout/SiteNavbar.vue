<script setup lang="ts">
import PageContainer from './PageContainer.vue'
import BaseButton from '../ui/BaseButton.vue'
</script>
<template>
  <header class="border-b border-navy/10 bg-white">
    <PageContainer
      ><nav
        aria-label="Primary"
        class="flex min-h-18 flex-wrap items-center justify-between gap-x-6"
      >
        <RouterLink to="/" class="inline-flex min-h-11 items-center text-xl font-semibold text-navy"
          >Ecodoo</RouterLink
        >
        <div
          class="order-3 flex w-full items-center gap-x-5 overflow-x-auto text-sm font-medium text-ink md:order-none md:w-auto md:gap-6"
        >
          <a class="inline-flex min-h-11 shrink-0 items-center" href="#platform">Platform</a
          ><a class="inline-flex min-h-11 shrink-0 items-center" href="#pillars">ESG pillars</a
          ><a class="inline-flex min-h-11 shrink-0 items-center" href="#traceability"
            >Traceability</a
          ><a class="inline-flex min-h-11 shrink-0 items-center" href="#trust">Trust</a>
        </div>
        <BaseButton href="/demo">View demo</BaseButton>
      </nav></PageContainer
    >
  </header>
</template>
