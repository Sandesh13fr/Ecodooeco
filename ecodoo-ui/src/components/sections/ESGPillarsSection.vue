<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
import SectionHeading from '../ui/SectionHeading.vue'
</script>
<template>
  <section id="pillars" class="bg-navy py-24 text-white sm:py-32">
    <PageContainer
      ><SectionHeading
        tone="inverse"
        title="Environmental, social, and governance—connected"
        description="Each pillar has its own controls while sharing one evidence model and reporting language."
      />
      <div class="mt-12 flex flex-col gap-8 lg:flex-row">
        <article
          v-for="item in [
            {
              t: 'Environment',
              c: 'text-teal',
              d: 'Emissions ledgers, factors, targets, and operational drivers.',
            },
            {
              t: 'Social',
              c: 'text-cobalt',
              d: 'Aggregated workforce measures with privacy-aware participation.',
            },
            {
              t: 'Governance',
              c: 'text-gold',
              d: 'Policies, acknowledgements, audits, and accountable issue closure.',
            },
          ]"
          :key="item.t"
          class="flex-1 border-t border-white/20 pt-6"
        >
          <h3 :class="['text-xl font-semibold', item.c]">{{ item.t }}</h3>
          <p class="mt-3 leading-7 text-white/80">{{ item.d }}</p>
        </article>
      </div></PageContainer
    >
  </section>
</template>
