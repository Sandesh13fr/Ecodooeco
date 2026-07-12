import { afterEach, describe, it, expect, vi } from 'vitest'

import { flushPromises, mount } from '@vue/test-utils'
import App from '../App.vue'
import router from '../router'
import HeroSection from '../components/sections/HeroSection.vue'

afterEach(() => vi.unstubAllGlobals())

describe('App', () => {
  it('renders the Ecodoo landing route', async () => {
    await router.push('/')
    await router.isReady()
    const wrapper = mount(App, { global: { plugins: [router] } })
    expect(wrapper.get('h1').text()).toContain('Every operation')
    expect(wrapper.find('a[href="#traceability"]').exists()).toBe(true)
    expect(wrapper.find('a[href="/app"]').exists()).toBe(true)
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
    expect(wrapper.get('h1').text()).toContain('Every operation')
    expect(wrapper.find('a[href="/app"]').exists()).toBe(true)
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

  it('renders the MVP command center and summary routes', async () => {
    await router.push('/app')
    await router.isReady()
    const wrapper = mount(App, { global: { plugins: [router] } })
    expect(wrapper.get('h1').text()).toContain('Command Center')
    expect(wrapper.text()).toContain('GreenRoute Logistics Pvt Ltd')
    expect(wrapper.text()).toContain('Demonstration management score')
    expect(wrapper.find('a[href="/app/transactions?role=manager"]').exists()).toBe(true)
    expect(wrapper.get('select').element.value).toBe('command-center')

    await wrapper.get('select').setValue('transactions')
    await flushPromises()
    expect(router.currentRoute.value.path).toBe('/app/transactions')

    await router.push('/app/summary?role=executive')
    await router.isReady()
    expect(wrapper.text()).toContain('One-page ESG Summary')
    expect(wrapper.text()).toContain('120.000 L x 2.680000 kg CO2e/L = 321.600 kg CO2e')
    expect(wrapper.text()).toContain('not independent assurance')
  })
})
