<script setup lang="ts">
const icons = {
  inbox: ['M3 4h14v12H3z', 'M3 12h4l1.5 2h3L13 12h4'],
  flask: ['M8 3v5l-4 7a1.5 1.5 0 0 0 1.3 2.2h9.4A1.5 1.5 0 0 0 16 15l-4-7V3', 'M7 11h6'],
  calculator: ['M5 3h10v14H5z', 'M7.5 6h5', 'M8 10h.01M12 10h.01M8 14h.01M12 14h.01'],
  target: ['M10 18a8 8 0 1 0-8-8', 'M10 14a4 4 0 1 0-4-4', 'M10 10l7-7', 'M13 3h4v4'],
  chart: ['M4 17V9', 'M10 17V5', 'M16 17v-4', 'M2 17h16'],
  link: ['M8 12l4-4', 'M7 15H5a3 3 0 0 1 0-6h3', 'M13 5h2a3 3 0 1 1 0 6h-3'],
  settings: [
    'M10 13a3 3 0 1 0 0-6 3 3 0 0 0 0 6z',
    'M16.5 11.5l1.2 1-.9 1.6-1.5-.5a7 7 0 0 1-1.3.8l-.3 1.6h-1.8l-.3-1.6a7 7 0 0 1-1.3-.8l-1.5.5-.9-1.6 1.2-1a7 7 0 0 1 0-1.5l-1.2-1 .9-1.6 1.5.5a7 7 0 0 1 1.3-.8l.3-1.6h1.8l.3 1.6a7 7 0 0 1 1.3.8l1.5-.5.9 1.6-1.2 1a7 7 0 0 1 0 1.5z',
  ],
  clipboard: ['M6 5H4v12h12V5h-2', 'M7 3h6v4H7z', 'M7 11h6M7 14h4'],
  lock: ['M5 9h10v8H5z', 'M7 9V7a3 3 0 0 1 6 0v2'],
} as const

defineProps<{ name: keyof typeof icons }>()
</script>

<template>
  <svg
    viewBox="0 0 20 20"
    fill="none"
    stroke="currentColor"
    stroke-width="1.5"
    stroke-linecap="round"
    stroke-linejoin="round"
    aria-hidden="true"
    focusable="false"
    :data-icon="name"
  >
    <path v-for="path in icons[name]" :key="path" :d="path" />
  </svg>
</template>
