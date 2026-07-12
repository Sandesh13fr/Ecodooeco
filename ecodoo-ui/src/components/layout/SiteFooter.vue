<script setup lang="ts">
import PageContainer from './PageContainer.vue'

const brandMark = '/graphics/ecodoo-mark.webp'
</script>

<template>
  <footer class="border-t border-white/8 bg-[#0a1628] py-10">
    <PageContainer>
      <div class="flex flex-col items-start justify-between gap-6 sm:flex-row sm:items-center">
        <div class="flex items-center gap-3">
          <img
            :src="brandMark"
            alt=""
            width="32"
            height="32"
            class="h-8 w-8 rounded-lg"
            aria-hidden="true"
          />
          <div>
            <p class="text-sm font-bold text-white">Ecodoo</p>
            <p class="text-xs text-white/40">Traceable ESG operations in Odoo</p>
          </div>
        </div>

        <!-- Center links -->
        <div class="flex flex-wrap gap-6 text-xs text-white/40">
          <a href="#platform" class="transition-colors hover:text-white">Platform</a>
          <a href="#pillars" class="transition-colors hover:text-white">ESG Pillars</a>
          <a href="#traceability" class="transition-colors hover:text-white">Evidence Trail</a>
          <a href="#trust" class="transition-colors hover:text-white">Trust</a>
        </div>

        <!-- Right -->
        <div class="flex items-center gap-4">
          <p class="text-xs text-white/30">© 2026 Ecodoo</p>
          <a
            href="#top"
            class="inline-flex h-8 items-center gap-1.5 rounded-lg border border-white/10 bg-white/5 px-3 text-xs font-medium text-white/50 transition-all hover:border-white/20 hover:text-white"
          >
            Back to top ↑
          </a>
        </div>
      </div>
    </PageContainer>
  </footer>
</template>
