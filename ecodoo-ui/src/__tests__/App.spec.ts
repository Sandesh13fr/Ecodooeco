import { afterEach, describe, it, expect, vi } from 'vitest'

import { mount } from '@vue/test-utils'
import App from '../App.vue'
import router from '../router'
import HeroSection from '../components/sections/HeroSection.vue'

afterEach(() => vi.unstubAllGlobals())

describe('App', () => {
  it('renders the Ecodoo landing route', async () => {
    await router.push('/')
    await router.isReady()
    const wrapper = mount(App, { global: { plugins: [router] } })
    expect(wrapper.get('h1').text()).toContain(
      'Operational activity becomes traceable ESG evidence',
    )
    expect(wrapper.find('a[href="#traceability"]').exists()).toBe(true)
    const video = wrapper.get('video')
    expect(video.attributes('autoplay')).toBeDefined()
    expect((video.element as HTMLVideoElement).muted).toBe(true)
    expect(video.attributes('playsinline')).toBeDefined()
    expect(video.attributes('poster')).toBe('/hero-poster.webp')
    expect(wrapper.get('source').attributes('src')).toBe('/hero-vedio.mp4')
    expect(wrapper.text()).toContain('SYNTHETIC-FUEL-2026 · v1')
    expect(wrapper.text()).toContain('Synthetic illustrative demo data')
    expect(wrapper.text()).toContain('6,028.80 kgCO₂e')
  })

  it('renders the demo route', async () => {
    await router.push('/demo')
    const wrapper = mount(App, { global: { plugins: [router] } })
    expect(wrapper.get('h1').text()).toContain('Trace an approved purchase')
    expect(wrapper.text()).toContain(
      'It is not a regulatory, audit, or carbon-neutrality certification.',
    )
    expect(wrapper.text()).toContain('PO-2026-0418')
  })

  it('uses the local hero video by default', () => {
    const wrapper = mount(HeroSection)
    expect(wrapper.get('source').attributes('src')).toBe('/hero-vedio.mp4')
    expect(wrapper.get('h1').text()).toContain(
      'Operational activity becomes traceable ESG evidence',
    )
    expect(wrapper.find('a[href="/demo"]').exists()).toBe(true)
  })

  it('uses the static hero surface when reduced motion is preferred', () => {
    vi.stubGlobal('matchMedia', () => ({
      matches: true,
      addEventListener: vi.fn<() => void>(),
      removeEventListener: vi.fn<() => void>(),
    }))
    const wrapper = mount(HeroSection)
    expect(wrapper.find('video').exists()).toBe(false)
    expect(wrapper.find('img[src="/hero-poster.webp"]').exists()).toBe(true)
  })
})
