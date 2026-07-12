<script setup lang="ts">
import PageContainer from '../components/layout/PageContainer.vue'
import BaseButton from '../components/ui/BaseButton.vue'
</script>
<template>
  <main class="min-h-screen bg-mist py-20">
    <PageContainer
      ><RouterLink to="/" class="inline-flex min-h-11 items-center font-semibold text-teal"
        >← Ecodoo home</RouterLink
      >
      <section class="mt-12 max-w-3xl">
        <p class="font-mono text-sm text-muted">DEMO SHELL</p>
        <h1 class="mt-4 text-4xl font-semibold">Trace an Odoo activity to its ESG result.</h1>
        <p class="mt-5 max-w-[65ch] text-lg leading-8 text-ink">
          The interactive product walkthrough will live here. This scaffold reserves the route
          without adding authentication or placeholder business logic.
        </p>
        <div class="mt-8">
          <BaseButton href="/#traceability" variant="secondary"
            >Review the evidence flow</BaseButton
          >
        </div>
      </section></PageContainer
    >
  </main>
</template>
