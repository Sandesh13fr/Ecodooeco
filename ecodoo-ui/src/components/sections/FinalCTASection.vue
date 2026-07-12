<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
import BaseButton from '../ui/BaseButton.vue'
</script>
<template>
  <section class="bg-navy py-20 text-white">
    <PageContainer
      ><div class="flex flex-col items-start justify-between gap-8 md:flex-row md:items-end">
        <div class="max-w-3xl">
          <h2 class="text-3xl font-semibold text-white sm:text-5xl">
            Trace one Odoo record all the way through.
          </h2>
          <p class="mt-4 max-w-[62ch] text-lg leading-8 text-white/80">
            Open the demo and inspect the source, factor, calculation, goal, and reporting path in
            context.
          </p>
        </div>
        <BaseButton href="/demo">Open the demo</BaseButton>
      </div></PageContainer
    >
  </section>
</template>
