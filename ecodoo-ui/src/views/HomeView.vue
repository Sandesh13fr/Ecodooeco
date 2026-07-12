<script setup lang="ts">
import SiteNavbar from '../components/layout/SiteNavbar.vue'
import SiteFooter from '../components/layout/SiteFooter.vue'
import HeroSection from '../components/sections/HeroSection.vue'
import PlatformOverviewSection from '../components/sections/PlatformOverviewSection.vue'
import ESGPillarsSection from '../components/sections/ESGPillarsSection.vue'
import TraceabilityFlowSection from '../components/sections/TraceabilityFlowSection.vue'
import CapabilitiesSection from '../components/sections/CapabilitiesSection.vue'
import TrustSection from '../components/sections/TrustSection.vue'
import FinalCTASection from '../components/sections/FinalCTASection.vue'
</script>
<template>
  <SiteNavbar />
  <main>
    <HeroSection />
    <PlatformOverviewSection />
    <ESGPillarsSection />
    <TraceabilityFlowSection />
    <CapabilitiesSection />
    <TrustSection />
    <FinalCTASection />
  </main>
  <SiteFooter />
</template>
