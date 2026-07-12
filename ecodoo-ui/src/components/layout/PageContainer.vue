<script setup lang="ts">
withDefaults(
  defineProps<{
    as?: 'div' | 'section'
    fullWidth?: boolean
  }>(),
  {
    as: 'div',
    fullWidth: false,
  },
)
</script>

<template>
  <component
    :is="as"
    :class="[
      'mx-auto w-full',
      fullWidth ? 'max-w-none px-4 sm:px-6 lg:px-8 xl:px-10' : 'max-w-7xl px-5 sm:px-8 lg:px-12',
    ]"
  >
    <slot />
  </component>
</template>
