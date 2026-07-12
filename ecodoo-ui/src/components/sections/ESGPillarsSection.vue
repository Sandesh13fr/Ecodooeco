<script setup lang="ts">
import PageContainer from '../layout/PageContainer.vue'
</script>
<template>
  <section id="pillars" class="bg-mist py-24 sm:py-32">
    <PageContainer>
      <h2 class="max-w-[17ch] text-3xl font-semibold sm:text-5xl">
        Three disciplines. One accountable operating model.
      </h2>
      <div class="mt-14 grid gap-10 lg:grid-cols-[1.2fr_0.9fr_1fr]">
        <article class="border-t-2 border-green pt-6">
          <p class="font-semibold text-green-ink">Environmental</p>
          <h3 class="mt-4 text-2xl font-semibold">Measure operational impact.</h3>
          <p class="mt-3 leading-7 text-muted">
            Build emissions ledgers from activity data, controlled factors, and explicit units.
          </p>
        </article>
        <article class="border-t-2 border-cobalt pt-6 lg:mt-16">
          <p class="font-semibold text-cobalt">Social</p>
          <h3 class="mt-4 text-2xl font-semibold">See progress without exposing people.</h3>
          <p class="mt-3 leading-7 text-muted">
            Track aggregate workforce measures with role-aware access and privacy.
          </p>
        </article>
        <article class="border-t-2 border-gold pt-6 lg:mt-28">
          <p class="font-semibold text-gold-ink">Governance</p>
          <h3 class="mt-4 text-2xl font-semibold">Turn policy into accountable action.</h3>
          <p class="mt-3 leading-7 text-muted">
            Manage policies, acknowledgements, audits, and issue closure in context.
          </p>
        </article>
      </div>
    </PageContainer>
  </section>
</template>
