<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
import SectionHeading from '../ui/SectionHeading.vue'
</script>
<template>
  <section id="platform" class="py-20 sm:py-24">
    <PageContainer
      ><SectionHeading
        title="One operating system for ESG evidence"
        description="Ecodoo works where finance, fleet, procurement, people, and governance records already live. Source context stays attached from capture to report."
      />
      <dl class="mt-12 grid gap-px overflow-hidden rounded-xl bg-navy/10 sm:grid-cols-3">
        <div
          v-for="item in [
            { t: 'Capture once', d: 'Use approved Odoo records as the operational source.' },
            {
              t: 'Calculate transparently',
              d: 'Retain quantities, units, factors, versions, and timestamps.',
            },
            {
              t: 'Act with context',
              d: 'Connect results to targets, issues, policies, and reports.',
            },
          ]"
          :key="item.t"
          class="bg-white p-7"
        >
          <dt class="font-semibold text-navy">{{ item.t }}</dt>
          <dd class="mt-2 leading-7 text-muted">{{ item.d }}</dd>
        </div>
      </dl></PageContainer
    >
  </section>
</template>
