<script setup lang="ts">
defineProps<{ as?: 'h1' | 'h2' }>()
</script>
<template>
  <component :is="as ?? 'h2'"><slot /></component>
</template>
