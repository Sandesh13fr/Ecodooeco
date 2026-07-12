<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
import SectionHeading from '../ui/SectionHeading.vue'
</script>
<template>
  <section id="capabilities" class="bg-mist py-20 sm:py-24">
    <PageContainer
      ><SectionHeading title="Built for the people responsible for the numbers" />
      <ul class="mt-10 grid gap-x-12 gap-y-8 sm:grid-cols-2">
        <li
          v-for="item in [
            'Operational data capture without duplicate entry',
            'Factor-versioned carbon calculations',
            'Goals and progress with source context',
            'Policies, audits, and governance issues',
            'Role-aware social measurement',
            'Management-ready ESG summaries',
          ]"
          :key="item"
          class="border-b border-navy/15 pb-6 font-medium text-navy"
        >
          {{ item }}
        </li>
      </ul></PageContainer
    >
  </section>
</template>
