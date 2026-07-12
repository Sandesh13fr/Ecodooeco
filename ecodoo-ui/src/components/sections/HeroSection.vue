<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import PageContainer from '../layout/PageContainer.vue'
import BaseButton from '../ui/BaseButton.vue'
import { useReducedMotion } from '../../composables/useReducedMotion'

const videoFailed = ref(false)
const { prefersReducedMotion } = useReducedMotion()
const videoUrl = '/hero-vedio.mp4'
const posterUrl = '/hero-poster.webp'

const scrollY = ref(0)
const handleScroll = () => {
  scrollY.value = window.scrollY
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
})
onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

const parallaxStyle = (factor: number) => ({
  transform: `translateY(${scrollY.value * factor}px)`,
})
</script>

<template>
  <section id="top" class="relative min-h-svh overflow-hidden bg-[#0a1628] text-white">
    <!-- ─── Background Video with Parallax ─── -->
    <div class="absolute inset-0 scale-110" :style="parallaxStyle(0.3)">
      <video
        v-if="!videoFailed && !prefersReducedMotion"
        class="h-full w-full object-cover"
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
        class="h-full w-full object-cover"
        aria-hidden="true"
        decoding="async"
        fetchpriority="high"
      />
    </div>

    <!-- ─── Multi-layer Cinematic Overlay ─── -->
    <div class="absolute inset-0" aria-hidden="true">
      <!-- Deep dark base -->
      <div class="absolute inset-0 bg-[#0a1628]/70"></div>
      <!-- Teal atmospheric bottom glow -->
      <div
        class="absolute bottom-0 left-0 right-0 h-[60%]"
        style="background: linear-gradient(to top, rgba(0, 201, 177, 0.12) 0%, transparent 100%)"
      ></div>
      <!-- Left vignette -->
      <div
        class="absolute inset-y-0 left-0 w-1/2"
        style="background: linear-gradient(to right, rgba(10, 22, 40, 0.6), transparent)"
      ></div>
      <!-- Top fade -->
      <div
        class="absolute inset-x-0 top-0 h-32"
        style="background: linear-gradient(to bottom, rgba(10, 22, 40, 0.8), transparent)"
      ></div>
      <!-- Subtle noise grain texture -->
      <div
        class="absolute inset-0 opacity-[0.03]"
        style="
          background-image: url('data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noise%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%224%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noise)%22/%3E%3C/svg%3E');
          background-size: 200px;
        "
      ></div>
    </div>

    <!-- ─── Hero Content ─── -->
    <PageContainer
      class="relative flex min-h-svh flex-col justify-end pb-16 pt-36 sm:pb-20 lg:pb-24"
    >
      <div class="max-w-5xl">
        <!-- Pill Badge -->
        <div class="animate-fade-up mb-6">
          <span class="pill-badge"> Environmental · Social · Governance </span>
        </div>

        <!-- Main Headline -->
        <h1
          class="animate-fade-up-delay-1 text-5xl font-extrabold leading-[1.02] sm:text-7xl lg:text-8xl"
        >
          <span class="block text-white">Every operation</span>
          <span class="mt-1 block accent-text">becomes ESG evidence.</span>
        </h1>

        <!-- Subtext -->
        <p
          class="animate-fade-up-delay-2 mt-6 max-w-[58ch] text-base leading-7 text-white/70 sm:text-lg sm:leading-8"
        >
          Ecodoo connects Odoo records to versioned emission factors, transparent calculations,
          governance workflows, and audit-ready reports — without spreadsheets.
        </p>

        <!-- CTA Buttons -->
        <div class="animate-fade-up-delay-3 mt-10 flex flex-wrap items-center gap-4">
          <a
            href="/app"
            class="group inline-flex items-center gap-2 rounded-xl bg-teal px-7 py-3.5 text-sm font-semibold text-white transition-all duration-300 hover:bg-teal-dark hover:shadow-[0_0_30px_rgba(0,201,177,0.4)] active:scale-95"
          >
            Explore the demo
            <svg
              class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
              viewBox="0 0 16 16"
              fill="none"
            >
              <path
                d="M3 8h10M9 4l4 4-4 4"
                stroke="currentColor"
                stroke-width="1.5"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </a>
          <a
            href="#traceability"
            class="inline-flex items-center gap-2 rounded-xl border border-white/20 px-7 py-3.5 text-sm font-semibold text-white/90 backdrop-blur-sm transition-all duration-300 hover:border-white/40 hover:bg-white/8 hover:text-white"
          >
            Follow the evidence trail
          </a>
        </div>

        <!-- Trust Indicators -->
        <div
          class="animate-fade-up-delay-3 mt-12 flex flex-wrap items-center gap-6 text-xs text-white/50"
        >
          <span class="flex items-center gap-2">
            <svg class="h-4 w-4 text-teal" viewBox="0 0 16 16" fill="currentColor">
              <path d="M8 1l1.9 3.9L14 5.6l-3 2.9.7 4.1L8 10.5l-3.7 2.1.7-4.1L2 5.6l4.1-.7L8 1z" />
            </svg>
            Native to Odoo 19
          </span>
          <span class="flex items-center gap-2">
            <svg
              class="h-4 w-4 text-teal"
              viewBox="0 0 16 16"
              fill="none"
              stroke="currentColor"
              stroke-width="1.5"
            >
              <path d="M8 14s-6-3.5-6-8a6 6 0 0112 0c0 4.5-6 8-6 8z" stroke-linecap="round" />
            </svg>
            Auditable by design
          </span>
          <span class="flex items-center gap-2">
            <svg
              class="h-4 w-4 text-teal"
              viewBox="0 0 16 16"
              fill="none"
              stroke="currentColor"
              stroke-width="1.5"
            >
              <path d="M2 8h12M8 2l6 6-6 6" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
            Full traceability
          </span>
        </div>
      </div>

      <!-- Scroll Indicator -->
      <div class="absolute bottom-8 right-8 hidden lg:flex scroll-indicator">
        <span
          class="text-xs font-medium tracking-widest text-white/30 uppercase"
          style="writing-mode: vertical-rl"
          >Scroll</span
        >
        <div class="scroll-indicator__line mt-3"></div>
      </div>
    </PageContainer>
  </section>
</template>
