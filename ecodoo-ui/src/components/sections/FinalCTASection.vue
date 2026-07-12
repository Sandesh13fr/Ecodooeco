<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
</script>

<template>
  <section class="relative overflow-hidden bg-[#0a1628] py-24 sm:py-32">
    <!-- Background video echo (subtle, blurred) -->
    <div class="pointer-events-none absolute inset-0" aria-hidden="true">
      <div
        class="absolute inset-0"
        style="
          background: linear-gradient(
            135deg,
            rgba(0, 201, 177, 0.08) 0%,
            transparent 60%,
            rgba(59, 130, 246, 0.06) 100%
          );
        "
      ></div>
      <!-- Animated glow orbs -->
      <div
        class="absolute -bottom-24 -left-24 h-96 w-96 animate-[float_8s_ease-in-out_infinite] rounded-full opacity-15"
        style="background: radial-gradient(circle, #00c9b1 0%, transparent 65%)"
      ></div>
      <div
        class="absolute -right-24 top-12 h-80 w-80 animate-[float_10s_ease-in-out_2s_infinite] rounded-full opacity-10"
        style="background: radial-gradient(circle, #3b82f6 0%, transparent 65%)"
      ></div>
    </div>

    <PageContainer class="relative">
      <div
        class="relative overflow-hidden rounded-3xl border border-white/10 bg-white/5 p-12 text-center backdrop-blur-sm sm:p-16 lg:p-20"
      >
        <!-- Inner glow border -->
        <div
          class="pointer-events-none absolute inset-0 rounded-3xl"
          style="
            box-shadow:
              inset 0 1px 0 rgba(255, 255, 255, 0.1),
              0 0 80px rgba(0, 201, 177, 0.08);
          "
          aria-hidden="true"
        ></div>

        <p class="mb-4 text-xs font-semibold uppercase tracking-widest text-teal">Get started</p>
        <h2 class="text-3xl font-bold text-white sm:text-5xl lg:text-6xl">
          Trace one Odoo record <br class="hidden sm:block" />
          <span class="accent-text">all the way through.</span>
        </h2>
        <p class="mx-auto mt-6 max-w-[60ch] text-base leading-7 text-white/60 sm:text-lg">
          Open the demo and inspect the source, factor, calculation, goal, and reporting path — all
          in context, all connected.
        </p>

        <!-- CTA -->
        <div class="mt-10 flex flex-col items-center gap-4 sm:flex-row sm:justify-center">
          <a
            href="/app"
            class="group inline-flex items-center gap-2.5 rounded-xl bg-teal px-8 py-4 text-base font-semibold text-white transition-all duration-300 hover:bg-teal-dark hover:shadow-[0_0_40px_rgba(0,201,177,0.35)] active:scale-95"
          >
            Open the demo
            <svg
              class="h-5 w-5 transition-transform duration-300 group-hover:translate-x-1"
              viewBox="0 0 20 20"
              fill="none"
            >
              <path
                d="M4 10h12M12 6l4 4-4 4"
                stroke="currentColor"
                stroke-width="1.5"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </a>
          <a
            href="#top"
            class="inline-flex items-center gap-2 text-sm font-medium text-white/50 transition-colors hover:text-white"
          >
            Back to top ↑
          </a>
        </div>

        <!-- Social proof row -->
        <div class="mt-12 flex flex-wrap items-center justify-center gap-8 text-xs text-white/35">
          <span>No credit card required</span>
          <span class="h-1 w-1 rounded-full bg-white/20"></span>
          <span>Live demo data</span>
          <span class="h-1 w-1 rounded-full bg-white/20"></span>
          <span>Built on Odoo 19</span>
          <span class="h-1 w-1 rounded-full bg-white/20"></span>
          <span>Open source module</span>
        </div>
      </div>
    </PageContainer>
  </section>
</template>
