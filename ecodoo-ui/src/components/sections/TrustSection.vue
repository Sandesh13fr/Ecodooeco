<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
import SectionHeading from '../ui/SectionHeading.vue'
</script>
<template>
  <section id="trust" class="bg-mist py-24 sm:py-32">
    <PageContainer
      ><div class="grid gap-12 lg:grid-cols-[0.9fr_1.1fr]">
        <SectionHeading
          title="Trust is visible in the record"
          description="Ecodoo identifies estimates and provenance. It supports management and disclosure work; it does not claim legal, audit, or regulatory certification."
        />
        <dl class="divide-y divide-navy/15 border-y border-navy/15">
          <div
            v-for="item in [
              ['Source lineage', 'Drill from a reported result to its originating Odoo record.'],
              [
                'Controlled calculation',
                'See quantity, units, conversion path, factor version, and timestamp.',
              ],
              [
                'Review history',
                'Retain approval state and correction history without rewriting the past.',
              ],
              [
                'Odoo permissions',
                'Respect company boundaries and role-based access throughout the trace.',
              ],
            ]"
            :key="item[0]"
            class="grid gap-2 py-5 sm:grid-cols-[10rem_1fr]"
          >
            <dt class="font-semibold text-navy">{{ item[0] }}</dt>
            <dd class="text-muted">{{ item[1] }}</dd>
          </div>
        </dl>
      </div></PageContainer
    >
  </section>
</template>
