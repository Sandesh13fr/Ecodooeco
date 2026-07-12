<script setup lang="ts">
withDefaults(
  defineProps<{
    href?: string
    variant?: 'primary' | 'secondary' | 'inverse'
    size?: 'default' | 'compact'
  }>(),
  { variant: 'primary', size: 'default' },
)
</script>
<template>
  <component
    :is="href ? 'a' : 'button'"
    :href="href"
    :type="href ? undefined : 'button'"
    class="inline-flex min-h-11 items-center justify-center rounded-lg font-semibold transition-[background-color,border-color,color,transform] duration-200 ease-out active:translate-y-px"
    :class="[
      size === 'compact' ? 'px-4 py-2 text-sm' : 'px-5 py-2.5 text-sm',
      variant === 'primary' && 'bg-teal text-white hover:bg-teal-dark',
      variant === 'secondary' &&
        'border border-navy/25 text-navy hover:border-navy/40 hover:bg-mist',
      variant === 'inverse' && 'border border-white/65 text-white hover:bg-white hover:text-navy',
    ]"
    ><slot
  /></component>
</template>
