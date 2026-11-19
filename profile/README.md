<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.png">
  <img alt="Creativate — AI research and consultancy, makers of c:node, Frankfurt. AI that has to justify its answers: a source for every statement, a record for every decision, and a person approving anything that leaves the system." src="assets/banner-light.png">
</picture>

[![c:node](https://img.shields.io/badge/product-c--node.ai-6B5BCD?style=flat-square)](https://c-node.ai)
[![Try c:node](https://img.shields.io/badge/try-try.c--node.ai-6B5BCD?style=flat-square)](https://try.c-node.ai)
[![c:node Graph](https://img.shields.io/badge/explore-c%3Anode%20Graph-4B6EF5?style=flat-square)](https://graph.c-node.ai)
[![creativate.tech](https://img.shields.io/badge/company-creativate.tech-1f2328?style=flat-square)](https://creativate.tech)
[![Book 30 minutes](https://img.shields.io/badge/book-30%20minutes-1a7f37?style=flat-square&logo=googlecalendar&logoColor=white)](https://calendar.app.google/wKQLGVxpP1n67fZL6)

[![EU AI Act](https://img.shields.io/badge/EU%20AI%20Act-Art.%2010%2C%2012%2C%2014-1f2328?style=flat-square)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
[![GDPR](https://img.shields.io/badge/GDPR-by%20design-1f2328?style=flat-square)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
![Hosting](https://img.shields.io/badge/hosting-EU%20(Frankfurt)%20%C2%B7%20on--premises%20%C2%B7%20air--gapped-36C399?style=flat-square)
![Identifiers](https://img.shields.io/badge/identifiers-ELI%20%C2%B7%20CELEX%20%C2%B7%20ECLI%20%C2%B7%20LEI-4B6EF5?style=flat-square)
![W3C](https://img.shields.io/badge/W3C-PROV--O%20%C2%B7%20SHACL-4B6EF5?style=flat-square)
![Vocabularies](https://img.shields.io/badge/vocabularies-EuroVoc%20%C2%B7%20NACE%20%C2%B7%20X%C3%96V%20%C2%B7%20FIM%2FLeiKa-4B6EF5?style=flat-square)
![Protocols](https://img.shields.io/badge/protocols-MCP%20%C2%B7%20OIDC%20%C2%B7%20OpenAPI-6B5BCD?style=flat-square)

We are an AI research and consultancy company from Frankfurt, Germany, and the team behind
**[c:node](https://c-node.ai)**.

Our work starts from one question: **how do you build AI that has to justify its answers?** Public
administrations, banks and the German Mittelstand cannot act on "the model said so". Every statement
needs a source someone can check, every decision a record, and nothing should leave the system
without a person approving it.

## What we work on

<table>
  <tr>
    <td width="33%" valign="top">
      <h3>Evidence for knowledge</h3>
      Answers grounded in a continuously growing knowledge graph of EU and German law, public registers and market
      data — with the norm, register entry or document each statement rests on.
    </td>
    <td width="33%" valign="top">
      <h3>Evidence for action</h3>
      Agents propose, people decide. Mails, tasks and changes in connected systems stay drafts until someone
      approves them, and every decision lands in an audit trail.
    </td>
    <td width="33%" valign="top">
      <h3>Sovereign by design</h3>
      EU hosting, GDPR and the EU AI Act built in, pseudonymisation before any external model call, and an
      on-premises edition down to air-gapped setups on open-weights models.
    </td>
  </tr>
</table>

## What we have built

| | |
|---|---|
| **[c:node](https://c-node.ai)** · platform | The product: a workspace that answers from your own documents and systems plus the graph, shows the source for each statement, and holds anything with an outside effect until a person approves it. Cloud, on-premises or air-gapped. [Try it](https://try.c-node.ai) · [Graph](https://graph.c-node.ai) · an MCP server for other tools to query |
| **c:node Graph** · research core | The continuously ingested knowledge graph behind the answers — EU and German law down to the article, public registers, procurement, market data. Grown under the rules written up in [governed-graph-growth](https://github.com/CreativateLabs/governed-graph-growth). |
| **[Zulano](https://www.zulano.io)** · public sector | Applications and funding research for public services. A data mesh of more than 34 million structured records as the grounding layer, and a rule-based service that routes a request to the responsible authority deterministically rather than by a model's guess. |
| **[AI Playbook](https://ai-playbook.creativate.tech)** · self-service | A trilingual AI readiness check for organisations starting out: a questionnaire in, a report out, with the GDPR and EU AI Act obligations that apply to what they described. |
| **Whitelabel instances** · pilots | The platform runs as a separate tenant per customer — own branding, own graph, own data boundary — for municipal and enterprise pilots. |
| **Consultancy** · discovery | Where it starts for most customers: a paid discovery that establishes whether the problem is one evidence-bound AI actually solves, and what it would cost to find out. |

## How c:node answers

```mermaid
flowchart LR
    Q["Question"] --> R{"Retrieve"}
    G[("c:node Graph<br/>law · registers · tenders · market")] --> R
    D[("Your organisation's<br/>documents & systems")] --> R
    R --> A["Answer<br/>with a source per statement"]
    A --> H{"Action with<br/>external effect?"}
    H -- "no" --> U["Answer to the user"]
    H -- "yes" --> P["Proposal card"] --> AP["Human approval"] --> X["Executed + logged"]
```

## The graph behind it

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/graph-dark.png">
  <img alt="The c:node Graph, figures as of November 2026: 52,000+ concepts, 106,000+ typed relations, 33 domains, 3.1 million+ company records, 51,000+ public tenders, 99.9%+ of concepts anchored to an official source." src="assets/graph-light.png">
</picture>

Live counts in the observatory at **[graph.c-node.ai](https://graph.c-node.ai)**, and the method
behind them in
**[governed-graph-growth](https://github.com/CreativateLabs/governed-graph-growth)**.

## Research

We publish **methods, not implementations**: how we evaluate, govern and grow systems that answer
with evidence, mapped to public standards so others can apply and check them.

| Publication | What it is | Cite |
|---|---|---|
| **[grounded-ai-evals](https://github.com/adminleo/grounded-ai-evals)** | A four-layer method for evaluating AI systems that answer with evidence — graph correctness, ontology hygiene, answer groundedness, baseline comparison — plus a release gate that blocks on named checks instead of a weighted mean. | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24100702.svg)](https://doi.org/10.5281/zenodo.24100702) |
| **[governed-graph-growth](https://github.com/CreativateLabs/governed-graph-growth)** | A technical note on keeping a continuously ingested, provenance-first knowledge graph trustworthy as it grows: source authority tiers, identity before enrichment, rule-classed linking, schema re-validation, growth health signals. | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24099664.svg)](https://doi.org/10.5281/zenodo.24099664) |

<img alt="Bundesministerium für Forschung, Technologie und Raumfahrt · BSFZ research allowance certified 2026 · EU AI Act · GDPR · member of the KI Bundesverband" src="assets/partners.png">

![EU-CORNET](https://img.shields.io/badge/consortium-EU--CORNET-4B6EF5?style=flat-square)
![Fraunhofer IVI](https://img.shields.io/badge/research%20partner-Fraunhofer%20IVI-4B6EF5?style=flat-square)
![MEF University](https://img.shields.io/badge/research%20partner-MEF%20University-4B6EF5?style=flat-square)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0005--6464--5179-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0009-0005-6464-5179)

## Work with us

- **Pilots** — public administrations, financial institutions and mid-sized companies that want AI they can audit:
  start at [c-node.ai](https://c-node.ai), or [book thirty minutes](https://calendar.app.google/wKQLGVxpP1n67fZL6).
- **Research** — universities and research institutes working on grounded AI, legal knowledge graphs or human
  oversight of AI agents: we are open to joint work and co-authored publications.
- **Contact** — [contact@creativate.tech](mailto:contact@creativate.tech) ·
  [Leonardo Bornhäußer](https://github.com/adminleo), CTO

<sub>Trust is good. Evidence is better.</sub>
