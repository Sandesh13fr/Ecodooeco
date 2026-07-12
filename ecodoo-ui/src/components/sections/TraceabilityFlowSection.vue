<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
import SectionHeading from '../ui/SectionHeading.vue'
</script>
<template>
  <section id="traceability" class="py-16 sm:py-20">
    <PageContainer
      ><SectionHeading
        title="A result you can trace back to work"
        description="Every material figure keeps the calculation path needed to review and reproduce it."
      />
      <ol
        class="mt-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5"
        aria-label="Evidence flow"
      >
        <li
          v-for="(step, index) in [
            'Odoo source record',
            'Activity and quantity',
            'Factor and version',
            'Carbon transaction',
            'Goal and report',
          ]"
          :key="step"
          class="flex flex-1 items-center gap-4 rounded-lg bg-mist p-5"
        >
          <span class="font-mono text-sm text-teal">{{ index + 1 }}</span
          ><span class="font-medium text-navy">{{ step }}</span>
        </li>
      </ol></PageContainer
    >
  </section>
</template>
