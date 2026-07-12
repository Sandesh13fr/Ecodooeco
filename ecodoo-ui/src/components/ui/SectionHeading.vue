<script setup lang="ts">
withDefaults(
  defineProps<{
    title: string
    description?: string
    align?: 'left' | 'center'
    tone?: 'default' | 'inverse'
  }>(),
  { tone: 'default' },
)
</script>

<template>
  <header :class="['max-w-3xl', align === 'center' && 'mx-auto text-center']">
    <h2 :class="['text-3xl font-semibold sm:text-4xl', tone === 'inverse' && 'text-white']">
      {{ title }}
    </h2>
    <p
      v-if="description"
      :class="[
        'mt-4 max-w-[70ch] text-base leading-7',
        tone === 'inverse' ? 'text-white/80' : 'text-muted',
      ]"
    >
      {{ description }}
    </p>
  </header>
</template>
