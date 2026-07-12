import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import App from '../App.vue'
import router from '../router'

describe('App', () => {
  it('renders the Ecodoo landing route', async () => {
    await router.push('/')
    await router.isReady()
    const wrapper = mount(App, { global: { plugins: [router] } })
    expect(wrapper.get('h1').text()).toContain('Odoo activity into traceable ESG evidence')
    expect(wrapper.find('a[href="#traceability"]').exists()).toBe(true)
  })
})
