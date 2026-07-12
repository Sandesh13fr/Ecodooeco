<script setup lang="ts">
import { ref } from 'vue'
import PageContainer from '../layout/PageContainer.vue'
import BaseButton from '../ui/BaseButton.vue'
import { useReducedMotion } from '../../composables/useReducedMotion'

const videoFailed = ref(false)
const { prefersReducedMotion } = useReducedMotion()
const videoUrl = '/hero-vedio.mp4'
const posterUrl = '/hero-poster.webp'
</script>

<template>
  <section id="top" class="relative min-h-svh overflow-hidden bg-navy text-white">
    <video
      v-if="!videoFailed && !prefersReducedMotion"
      class="absolute inset-0 h-full w-full object-cover"
      autoplay
      muted
      loop
      playsinline
      preload="metadata"
      :poster="posterUrl"
      aria-hidden="true"
      @error="videoFailed = true"
    >
      <source :src="videoUrl" type="video/mp4" />
    </video>
    <img
      v-else
      :src="posterUrl"
      alt=""
      class="absolute inset-0 h-full w-full object-cover"
      aria-hidden="true"
      decoding="async"
      fetchpriority="high"
    />
    <div class="absolute inset-0 bg-navy/75" aria-hidden="true"></div>
    <PageContainer class="relative flex min-h-svh items-end pb-12 pt-32 sm:pb-16 lg:pb-20">
      <div class="max-w-4xl">
        <p
          class="mb-5 inline-flex rounded-full border border-white/30 bg-navy/80 px-4 py-2 text-sm font-semibold text-white"
        >
          Environmental · Social · Governance, native to Odoo
        </p>
        <h1
          class="max-w-[15ch] text-4xl font-semibold leading-[1.04] text-white sm:text-6xl lg:text-7xl"
        >
          Operational activity becomes traceable ESG evidence.
        </h1>
        <p class="mt-6 max-w-[62ch] text-base leading-7 text-white sm:text-lg">
          Ecodoo connects Odoo records to versioned factors, transparent calculations, goals,
          governance actions, and reports—without rebuilding the evidence in spreadsheets.
        </p>
        <div class="mt-8 flex flex-wrap gap-3">
          <BaseButton href="/demo">Explore the demo</BaseButton>
          <BaseButton href="#traceability" variant="inverse">Follow the evidence trail</BaseButton>
        </div>
      </div>
    </PageContainer>
  </section>
</template>
