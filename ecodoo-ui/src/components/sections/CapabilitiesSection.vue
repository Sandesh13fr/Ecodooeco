<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
import SectionHeading from '../ui/SectionHeading.vue'
</script>
<template>
  <section id="capabilities" class="py-20 sm:py-24">
    <PageContainer>
      <SectionHeading
        title="From evidence to the next decision"
        description="Ecodoo keeps measurement, management, and reporting connected without turning the homepage into a wall of widgets."
      />
      <div class="mt-12 grid gap-x-12 gap-y-10 md:grid-cols-2">
        <article
          v-for="item in [
            [
              'Carbon transactions',
              'Create reproducible entries from Odoo activity and immutable factor versions.',
            ],
            ['Goals and progress', 'Connect each result to a baseline, target, owner, and period.'],
            [
              'Governance workflow',
              'Assign policy acknowledgements, audits, findings, and corrective actions.',
            ],
            [
              'Management reports',
              'Produce clear summaries with estimates, provenance, and drill-down intact.',
            ],
          ]"
          :key="item[0]"
          class="border-b border-navy/15 pb-8"
        >
          <h3 class="text-xl font-semibold">{{ item[0] }}</h3>
          <p class="mt-3 max-w-[58ch] leading-7 text-muted">{{ item[1] }}</p>
        </article>
      </div>
    </PageContainer>
  </section>
</template>
