<script setup lang="ts">
withDefaults(defineProps<{ href?: string; variant?: 'primary' | 'secondary' }>(), {
  variant: 'primary',
})
</script>

<template>
  <component
    :is="href ? 'a' : 'button'"
    :href="href"
    class="inline-flex min-h-11 items-center justify-center rounded-lg px-5 py-2.5 text-sm font-semibold transition-colors duration-200"
    :class="
      variant === 'primary'
        ? 'bg-teal text-white hover:bg-navy'
        : 'border border-navy/20 text-navy hover:bg-mist'
    "
  >
    <slot />
  </component>
</template>
