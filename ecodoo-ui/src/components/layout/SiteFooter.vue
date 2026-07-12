<script setup lang="ts">
import PageContainer from './PageContainer.vue'
</script>

<template>
  <footer class="border-t border-white/8 bg-[#0a1628] py-10">
    <PageContainer>
      <div class="flex flex-col items-start justify-between gap-6 sm:flex-row sm:items-center">
        <!-- Brand -->
        <div class="flex items-center gap-3">
          <div class="flex h-8 w-8 items-center justify-center rounded-lg bg-teal/20 ring-1 ring-teal/30">
            <svg class="h-4 w-4 text-teal" viewBox="0 0 16 16" fill="none">
              <path d="M8 2L2 6v8h4v-4h4v4h4V6L8 2z" stroke="currentColor" stroke-width="1.2" stroke-linejoin="round" fill="rgba(0,201,177,0.2)"/>
            </svg>
          </div>
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
