<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
import BaseButton from '../ui/BaseButton.vue'
import AnimatedHeading from '../motion/AnimatedHeading.vue'
</script>
<template>
  <section id="top" class="bg-mist py-20 sm:py-28">
    <PageContainer
      ><div class="max-w-4xl">
        <p class="mb-5 font-medium text-teal">ESG management, native to Odoo</p>
        <AnimatedHeading as="h1" class="text-4xl font-semibold leading-tight sm:text-6xl"
          >Turn everyday Odoo activity into traceable ESG evidence.</AnimatedHeading
        >
        <p class="mt-6 max-w-[68ch] text-lg leading-8 text-ink">
          Ecodoo connects operational records to factor-versioned measurements, goals, governance
          actions, and clear reports—without rebuilding your data in spreadsheets.
        </p>
        <div class="mt-9 flex flex-wrap gap-3">
          <BaseButton href="/demo">Explore the demo</BaseButton
          ><BaseButton href="#traceability" variant="secondary"
            >Follow the evidence trail</BaseButton
          >
        </div>
      </div></PageContainer
    >
  </section>
</template>
