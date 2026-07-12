import { onBeforeUnmount, onMounted, ref } from 'vue'

export function useReducedMotion() {
  const prefersReducedMotion = ref(
    typeof window !== 'undefined' && typeof window.matchMedia === 'function'
      ? window.matchMedia('(prefers-reduced-motion: reduce)').matches
      : false,
  )
  let query: MediaQueryList | undefined
  const update = () => {
    prefersReducedMotion.value = query?.matches ?? false
  }
  onMounted(() => {
    if (typeof window.matchMedia !== 'function') return
    query = window.matchMedia('(prefers-reduced-motion: reduce)')
    update()
    query.addEventListener('change', update)
  })
  onBeforeUnmount(() => query?.removeEventListener('change', update))
  return { prefersReducedMotion }
}
