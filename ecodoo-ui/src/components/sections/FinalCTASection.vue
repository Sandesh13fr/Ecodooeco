<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
import BaseButton from '../ui/BaseButton.vue'
</script>
<template>
  <section class="bg-navy py-16 text-white">
    <PageContainer
      ><div class="flex flex-col items-start justify-between gap-8 md:flex-row md:items-center">
        <div class="max-w-2xl">
          <h2 class="text-3xl font-semibold text-white">See the evidence trail in context.</h2>
          <p class="mt-3 text-white/80">Walk from an Odoo record to a traceable ESG result.</p>
        </div>
        <BaseButton href="/demo">Open demo shell</BaseButton>
      </div></PageContainer
    >
  </section>
</template>
