<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import PageContainer from './PageContainer.vue'
import BaseButton from '../ui/BaseButton.vue'

const scrolled = ref(false)
const mobileMenuOpen = ref(false)

const handleScroll = () => {
  scrolled.value = window.scrollY > 40
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
})
onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

const navLinks = [
  { label: 'Platform', href: '#platform' },
  { label: 'ESG Pillars', href: '#pillars' },
  { label: 'Evidence Trail', href: '#traceability' },
  { label: 'Trust', href: '#trust' },
]
</script>

<template>
  <header
    class="fixed inset-x-0 top-0 z-50 transition-all duration-500"
    :class="scrolled ? 'py-2' : 'py-4'"
  >
    <PageContainer>
      <nav
        aria-label="Primary"
        class="flex min-h-14 items-center justify-between gap-6 rounded-2xl px-5 transition-all duration-500 sm:px-6"
        :class="scrolled
          ? 'border border-white/10 bg-[#0a1628]/90 shadow-[0_8px_32px_rgba(0,0,0,0.4)] backdrop-blur-xl'
          : 'border border-white/8 bg-[#0a1628]/50 backdrop-blur-md'"
      >
        <!-- Logo -->
        <RouterLink
          to="/"
          class="inline-flex items-center gap-2.5 text-lg font-bold text-white tracking-tight"
        >
          <div class="flex h-8 w-8 items-center justify-center rounded-lg bg-teal/20 ring-1 ring-teal/40">
            <svg class="h-4 w-4 text-teal" viewBox="0 0 16 16" fill="none">
              <path d="M8 2L2 6v8h4v-4h4v4h4V6L8 2z" stroke="currentColor" stroke-width="1.2" stroke-linejoin="round" fill="rgba(0,201,177,0.2)"/>
            </svg>
          </div>
          <span>Ecodoo</span>
        </RouterLink>

        <!-- Desktop Nav Links -->
        <div class="hidden items-center gap-1 lg:flex">
          <a
            v-for="link in navLinks"
            :key="link.href"
            :href="link.href"
            class="inline-flex h-9 items-center rounded-lg px-3 text-sm font-medium text-white/70 transition-all duration-200 hover:bg-white/8 hover:text-white"
          >
            {{ link.label }}
          </a>
        </div>

        <!-- Right CTA -->
        <div class="flex items-center gap-3">
          <a
            href="/demo"
            class="inline-flex h-9 items-center justify-center gap-1.5 rounded-xl bg-teal px-4 text-sm font-semibold text-white transition-all duration-200 hover:bg-teal-dark hover:shadow-[0_0_20px_rgba(0,201,177,0.3)] active:scale-95"
          >
            View demo
            <svg class="h-3.5 w-3.5" viewBox="0 0 14 14" fill="none">
              <path d="M2.5 7h9M8 3l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>

          <!-- Mobile Menu Button -->
          <button
            class="inline-flex h-9 w-9 items-center justify-center rounded-lg border border-white/15 text-white/70 transition-all hover:bg-white/8 hover:text-white lg:hidden"
            :aria-expanded="mobileMenuOpen"
            aria-label="Toggle menu"
            @click="mobileMenuOpen = !mobileMenuOpen"
          >
            <svg v-if="!mobileMenuOpen" class="h-5 w-5" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M3 6h14M3 10h14M3 14h14" stroke-linecap="round"/>
            </svg>
            <svg v-else class="h-5 w-5" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M5 5l10 10M15 5L5 15" stroke-linecap="round"/>
            </svg>
          </button>
        </div>
      </nav>

      <!-- Mobile Menu -->
      <div
        v-if="mobileMenuOpen"
        class="mt-2 rounded-2xl border border-white/10 bg-[#0a1628]/95 p-4 backdrop-blur-xl lg:hidden"
      >
        <a
          v-for="link in navLinks"
          :key="link.href"
          :href="link.href"
          class="flex h-11 items-center rounded-xl px-4 text-sm font-medium text-white/80 transition-all hover:bg-white/8 hover:text-white"
          @click="mobileMenuOpen = false"
        >
          {{ link.label }}
        </a>
      </div>
    </PageContainer>
  </header>
</template>
