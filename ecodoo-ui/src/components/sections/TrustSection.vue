<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
import SectionHeading from '../ui/SectionHeading.vue'
</script>
<template>
  <section id="trust" class="py-20 sm:py-24">
    <PageContainer
      ><div class="grid gap-10 lg:grid-cols-[1fr_1.1fr]">
        <SectionHeading
          title="Trust comes from visible limits and evidence"
          description="Ecodoo identifies estimates and provenance. It supports management and disclosure work; it does not claim legal, audit, or regulatory certification."
        />
        <dl class="divide-y divide-navy/10 border-y border-navy/10">
          <div
            v-for="item in [
              {
                t: 'Reproducible',
                d: 'Units, conversion path, result, and calculation time retained.',
              },
              {
                t: 'Controlled',
                d: 'Odoo permissions, company boundaries, and approval workflows respected.',
              },
              {
                t: 'Reviewable',
                d: 'Source records and corrections remain available from the result.',
              },
            ]"
            :key="item.t"
            class="py-5"
          >
            <dt class="font-semibold text-navy">{{ item.t }}</dt>
            <dd class="mt-1 text-muted">{{ item.d }}</dd>
          </div>
        </dl>
      </div></PageContainer
    >
  </section>
</template>
