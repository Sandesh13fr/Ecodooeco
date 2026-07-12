<script setup lang="ts">
defineProps<{ as?: 'div' | 'section' }>()
</script>

<template>
  <component :is="as ?? 'div'" class="mx-auto w-full max-w-7xl px-5 sm:px-8 lg:px-12">
    <slot />
  </component>
</template>
