\partpage{01}{UNDERSTAND}{Map who can reach people, keys, devices, and routines.}


# Physical Security

> **KEY TAKEAWAY.** Physical security protects people and assets from threats that bypass cryptography entirely:
> coercion, theft, surveillance, and tampering. It is a distinct domain from operational security, addressing bodily
> harm, forced access, and physical integrity rather than information disclosure.

Cryptography and digital controls protect keys and data from algorithmic and remote attack. They do not protect the
people who hold those keys from physical threats, nor the hardware and facilities those keys depend on. Physical
security is the domain that addresses these threats directly: protecting people from harm and coercion, protecting
physical assets from theft and tampering, detecting physical surveillance, and preserving the integrity of the hardware
supply chain.

## What physical security covers

- **People:** Protection from bodily harm, forced access, kidnapping, and coercion of key-holders and their families.
- **Physical assets:** Protection of devices, backups, and facilities from theft, destruction, and unauthorized access.
- **Counter-surveillance:** Detecting and countering physical surveillance that precedes targeted attacks.
- **Supply chain integrity:** Tamper evidence and provenance for the hardware that custodies keys.

## Relationship to Operational Security

Physical security and [Operational Security](https://frameworks.securityalliance.dev/opsec/overview) are distinct but overlapping domains:

- **Operational Security** mitigates information disclosure through procedural and digital controls. Its goal is to
  reduce what an adversary can learn.
- **Physical Security** mitigates bodily harm, forced access, and physical tampering through barriers, deterrence,
  deception, and response. Its goal is to reduce what an adversary can physically do.

Overlap areas - such as travel safety and device theft - are handled by cross-references rather than duplication. Where
OpSec guidance touches physical coercion (for example, duress codes or border inspections), it links here rather than
restating the controls.

## What this framework covers

- [**Coercion & Duress**](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/overview) - Defending key-holders against wrench
  attacks: coercion, kidnapping, and extortion targeting the people who control keys. This is the most developed
  sub-section of the framework.
- [**Facility & Perimeter Security**](https://frameworks.securityalliance.dev/physical-security/facility-and-perimeter/overview) - Access control,
  surveillance, environmental controls, and secure facility design. *(In progress.)*
- [**Physical Counter-Surveillance**](https://frameworks.securityalliance.dev/physical-security/physical-counter-surveillance/overview) - Detecting and
  countering physical surveillance of people and locations. *(In progress.)*
- [**Supply Chain Physical Integrity**](https://frameworks.securityalliance.dev/physical-security/supply-chain-physical-integrity/overview) - Tamper evidence
  and hardware provenance for devices that custody keys. *(In progress.)*

## Related frameworks

- [Operational Security](https://frameworks.securityalliance.dev/opsec/overview) - information disclosure and routine OPSEC
- [Wallet Security](https://frameworks.securityalliance.dev/wallet-security/overview) - technical custody and wallet controls
- [Incident Management](https://frameworks.securityalliance.dev/incident-management/overview) - general incident response
- [Supply Chain Security](https://frameworks.securityalliance.dev/supply-chain/overview) - software and vendor supply chain
- [Treasury Operations](https://frameworks.securityalliance.dev/treasury-operations/overview) - organizational treasury process

## Who this framework serves

This framework serves individuals (founders, traders, KOLs) and organizations (exchanges, funds, DAOs, and protocols)
that control significant on-chain or custodial balances, as well as anyone whose role makes them a target for physical
attack because of the assets they can access.


# How to Protect Against Wrench Attacks

> **KEY TAKEAWAY.** Physical attacks bypass technical security by coercing the people who hold keys. As self-custody
> and on-chain treasuries grow, this threat vector now affects individuals and organizations alike, demanding dedicated
> controls beyond cryptography.

This page is the overview of the **Coercion & Duress** sub-section of the
[Physical Security](https://frameworks.securityalliance.dev/physical-security/overview) framework. It focuses specifically on wrench
attacks: coercion of the people who control keys. For other physical security domains, see the
[Physical Security overview](https://frameworks.securityalliance.dev/physical-security/overview).

Cryptography protects keys from algorithmic attack, not from coercion of the people who hold them. As self-custody,
on-chain treasuries, and high-profile crypto-native individuals become more common, adversaries increasingly bypass
technical defenses by targeting people directly through threats, surveillance, kidnapping, or extortion. These are
commonly referred to as **wrench attacks**.

## What is a wrench attack?

A wrench attack is any situation where an attacker bypasses technical security by directly targeting the person who
controls the keys. Unlike phishing, malware, or protocol exploits, wrench attacks assume the attacker has physical
proximity or credible reach to the victim, and that technical controls alone are insufficient.

The term originates from the [xkcd webcomic](https://xkcd.com/538/), which satirically illustrated
that sophisticated 4096-bit RSA encryption could be bypassed more effectively by a $5 wrench than by
a supercomputer.

## Why this matters now

- Growth of self-custody, non-custodial wallets, and on-chain treasuries means more value is directly controlled by a
  small number of individuals, often without institutional physical security.
- Public on-chain data, social media signaling, and leaks make it easier for adversaries to identify likely high-value
  targets and correlate them with real-world identities.
- Existing wallet security guidance focuses mainly on technical compromise, leaving physical and social-engineering
  vectors underserved.

## Scope

This sub-section covers individuals (founders, traders, KOLs) and organizations such as crypto exchanges, funds, DAOs,
and protocols operating with significant on-chain or custodial balances.

It assumes that adversaries can use basic OSINT, social engineering, and physical surveillance to find and pressure
key-holders.

## Related frameworks

- [Physical Security overview](https://frameworks.securityalliance.dev/physical-security/overview)
- [Wallet Security](https://frameworks.securityalliance.dev/wallet-security/overview)
- [Operational Security](https://frameworks.securityalliance.dev/opsec/overview)
- [Incident Management](https://frameworks.securityalliance.dev/incident-management/overview)


# Threat Model

> **KEY TAKEAWAY.** Wrench attackers range from opportunistic criminals to organized crime, insiders, and state
> actors. Their objectives span direct theft, extortion, operational coercion, and intelligence gathering, executed
> across residential, workplace, public, and family-adjacent attack surfaces.

Wrench attacks rely on coercing people, not breaking cryptography. This section characterizes who the adversaries are,
what they want, and where they are most likely to strike, so that wallet and key setups can be aligned to real-world
risk instead of purely technical assumptions.

## Attacker types

- **Opportunistic criminals:** Street-level or local gangs who become aware that a target "has crypto" (through social
  media, lifestyle, or loose talk) and attempt fast, high-pressure extortion with limited technical skills. These actors
  typically aim for immediate liquid funds (hot wallets, exchange accounts) and are more sensitive to time pressure and
  visible risk.
- **Organized crime groups:** Structured groups that combine OSINT, surveillance, and insider recruitment to identify
  and pressure high-value key-holders, including founders and treasury staff.
- **Insiders and close circle:** Current or former employees, contractors, business partners, family members, or
  intimate partners who know or suspect that the victim controls significant digital assets. They often possess
  contextual knowledge (where devices are, when approvals happen, who else can sign), making them especially dangerous
  in blended social-physical attacks.
- **State actors:** Security services, law-enforcement units, or proxy groups in jurisdictions with weak rule of law or
  hostile regulatory environments, using detention, travel stops, or raids to obtain keys or force on-chain actions.

## Attacker objectives

- **Direct theft:** Forcing the victim to unlock devices, disclose seed phrases, or sign transactions to transfer funds
  to attacker-controlled addresses.
- **Extortion and blackmail:** Using threats of continued violence, exposure, or reputational damage to demand repeated
  payments over time. May target both personal funds and organizational treasuries.
- **Operational coercion:** Forcing specific on-chain actions: pausing or upgrading contracts, whitelisting addresses,
  approving malicious proposals, or leaking internal secrets and signing policies.
- **Intelligence gathering:** Mapping the organization's wallet architecture, signing processes, key-holders, and
  recovery mechanisms for future operations.

## Attack surfaces

- **Residential environment:** Home invasions, confrontations in building common areas, parking ambushes, and threats
  involving family members or roommates.
- **Workplace:** Approaching treasury, operations, or engineering staff near the office, parking areas, or on their
  commute home. Risks increase when work devices with wallet access leave secure premises or when visitors can move
  freely inside office spaces.
- **Public spaces:** Incidents in cafés, restaurants, airports, hotels, or nightlife locations where routine patterns
  are easy to observe. Crypto events (conferences, side-events) are particularly attractive hunting grounds, as they
  densely concentrate potential targets.
- **Family, friends, and staff:** Threats directed at spouses, partners, children, drivers, assistants, or security
  staff, who may have indirect access. Attackers can also use them as leverage.

## Further reading

- [Coercion & Duress overview](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/overview): how the pages of this sub-section fit
  together
- [Risk Factors and Early Signals](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/risk-factors-and-early-signals): how these
  attackers select and approach targets
- [Defensive Design Principles](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/defensive-design-principles): the controls that
  answer this threat model
- [Threat Modeling](https://frameworks.securityalliance.dev/threat-modeling/overview): a structured method for building your own


# Risk Factors and Early Signals

> **KEY TAKEAWAY.** Public visibility, predictable routines, concentrated key-holder power, weak governance, and
> high-risk geographies amplify wrench-attack exposure. Reconnaissance patterns, targeted doxxing, and unfamiliar
> surveillance often precede physical attempts, providing critical warning windows when monitored.

## Individual risk factors

Public visibility and signaling are among the strongest individual risk amplifiers for wrench attacks. Founders, KOLs,
traders, and engineers who publicly reference large fundraising rounds, trading gains, or treasury balances
substantially increase their appeal as targets.

Lifestyle choices and daily routines further magnify this exposure by making physical access both predictable and
low-cost. Conspicuous displays of wealth, such as luxury cars, expensive accessories, or frequent premium travel,
combined with repetitive behaviors enable even rudimentary surveillance to identify favorable moments for intervention.

Operating from unsecured home environments while routinely approving high-value transactions also collapses digital
control and physical presence into the same space, centralizing financial risk and personal safety threats on a single
individual.

## Organizational risk factors

Organizational risk factors primarily stem from concentrated key-holder power and weak separation of duties, which
create high-value targets for wrench attacks. When a single individual can authorize major treasury movements, physical
coercion becomes an efficient path to theft.

Poor governance exacerbates this risk by treating key management as a purely technical function, disconnected from
physical security and HR oversight, leaving key exposures unaddressed during hiring, role transitions, or travel.

## Environmental and geographic risk factors

Regions with high rates of violent crime, weak law enforcement, or corruption raise the baseline probability that
crypto-related targets will be identified and approached. Travel to jurisdictions with aggressive or opaque enforcement
practices increases the risk of "official" coercion at borders, hotels, or offices.

## Early signals and pre-incident indicators

- **OSINT and probing behavior:** Unusual follower spikes, repeated DMs asking operational questions, or detailed
  probing about treasury structure, custody, or personal routines can signal reconnaissance. Repeated appearance of
  unfamiliar individuals around home or office should be treated as a potential warning.
- **Escalating threats and doxxing:** Targeted harassment, threats mentioning family, or doxxing posts linking real
  identity to wallet addresses or balances often precede physical attempts. Leaks of internal documents or partial leaks
  of residential or work addresses can also mark a shift from opportunistic to targeted risk.

## Further reading

- [Coercion & Duress overview](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/overview): how the pages of this sub-section fit
  together
- [Threat Model](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/threat-model): who acts on these signals and why
- [Personal and Family Safety](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/personal-and-family-safety): reducing the
  exposure these factors describe
- [Digital Footprint](https://frameworks.securityalliance.dev/privacy/digital-footprint): the public information attackers use to select targets


\partpage{02}{DESIGN}{Make coercion of one person insufficient.}


# Defensive Design Principles

> **KEY TAKEAWAY.** Five principles anchor wrench-attack defense: minimization limits what any coerced individual can
> authorize; compartmentalization segments keys and roles; controlled surrender offers a believable low-value payout
> while real reserves sit behind visible delay; resilience enables recovery; prioritization always favors human safety
> over assets.

These principles guide all subsequent controls, ensuring wallet architectures and operational processes withstand
coercion without relying solely on the victim's resistance under extreme pressure.

## Minimization

- Minimize the value and impact of what any single coerced individual can authorize during a time-constrained attack
  window.
- Design wallet tiers and signing limits so that even full compliance yields only low-to-moderate losses, forcing
  attackers to sustain operations longer and increasing their detection risk.

## Compartmentalization

- Segment keys, identities, devices, locations, and roles to prevent compromise of one element from cascading across the
  entire stack.
- Separate hot wallets for daily ops from cold storage for long-term holdings, and distribute signer responsibilities
  across jurisdictions, risk profiles, and access methods.

## Controlled surrender

- Offer attackers a small, believable payout they can take immediately, such as a low-value wallet with balances
  matching the victim's public profile.
- Keep strategic reserves behind time-locks and multi-party approval whose delay is visible and cannot be shortened
  under coercion.
- Wire duress wallets to fund-movement alerts that notify trusted contacts silently, enabling distress signaling without
  any call or text from the victim.

## Resilience

- Design for post-incident recovery without single points of failure.
- Protect human factors: avoid blame cycles, control information flows to prevent secondary leaks or attrition.
- Maintain operational continuity through distributed knowledge and pre-tested reconstruction.

## Prioritization

- Sequence all controls to favor human safety over assets during active threats.
- No policy should incentivize physical resistance; wallet rules yield immediately to safety triggers.
- Integrate with physical security, crisis management, and law enforcement protocols.

## Further reading

- [Coercion & Duress overview](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/overview): how the pages of this sub-section fit
  together
- [Wallet and Key Architecture](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/wallet-and-key-architecture): minimization and
  compartmentalization applied to keys
- [Transaction Flows Under Duress](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/transaction-flows-under-duress): controlled
  surrender in the signing path
- [Checklist](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/checklist): turning these principles into sequenced work


# Wallet and Key Architecture

> **KEY TAKEAWAY.** Tiered wallet structures (hot, warm, cold, deep-cold) combined with multisig or MPC, geographic
> key distribution, controlled-surrender wallets, and rotation policies ensure no single coerced individual can drain
> strategic reserves under pressure.

## Wallet strategy

- **Hot wallets (0-1% of total value):** Daily operational funds on L1/L2 for gas, small payments, emergency liquidity.
  Strict daily spend limits (under $10k equivalent), no direct path to cold storage.
- **Warm wallets (1-5%):** Short-term operational (1-7 days) funds for payroll, vendor payments, marketing. Geo-fenced
  approvals, multisig with time delays for larger moves.
- **Cold wallets (5-25%):** Medium-term holdings accessible within 24-72 hours via hardware signers. Stored in bank
  vaults or secure facilities, never at primary residence or office.
- **Deep-cold (remaining balance):** Strategic reserves in air-gapped HSMs, multi-party custodians, or institutional
  custody. Recovery requires legal processes or key ceremonies spanning weeks.

## Multisig and MPC

- **Multisig setups:** Minimum 3-of-5 or 4-of-7 signers for any material movement; distribute across geographies and
  risk profiles so coercing one person blocks action.
- **MPC (multi-party computation):** Threshold schemes where no single key share enables spending.

## Geographically decoupled key storage

- **Primary residence:** Never store hardware wallets, seeds, or signer devices. Use only temporary hot wallet access
  via secure elements (YubiKey, phone-bound keys).
- **Secure offsite locations:** Bank safety deposit boxes, private vaults, or trusted family abroad for cold wallet
  hardware.
- **Institutional custodians:** Fireblocks, Copper, or regulated providers for deep-cold.
- **Smart contract guardians:** Protocol-level treasuries use on-chain timelocks, pause functions, or emergency multisig
  for protocol upgrades under duress.

## Controlled-surrender wallets and duress tripwires

- **Readily-surrendered funds:** Keep one small wallet ($2k-$5k, with balances matching observed transaction patterns)
  that can be handed over truthfully under duress, rather than relying on a lie that may fail under stress. Seeds and
  PINs memorized separately for handover.
- **Visible friction on real reserves:** Use on-chain time-locks, multisig, and multi-party approval on strategic funds
  so larger amounts demonstrably cannot be moved quickly, reducing the attacker's incentive to keep coercing.
- **Duress tripwires:** Tie the small wallet's duress PIN to silent alerts that notify trusted contacts and, where
  appropriate, law enforcement.
- **Burner exchange accounts:** Pre-funded CEX accounts (around $10k) linked to public personas, for immediate handover
  without touching core holdings.

## Key ceremonies and rotation policies

- **Initial key ceremonies:** Conducted in neutral third-party locations with video audit trails. Mnemonic shards split
  across a minimum of 3 participants, never whole seeds.
- **Periodic rotations:** Quarterly review of signer eligibility. Annual full key refresh with new hardware and devices.
  Trigger rotations after travel to high-risk jurisdictions.
- **Post-incident rotation:** Pre-defined playbook for 24-hour signer replacement, contract migrations, and full-stack
  rebuild without single points of failure.

## Further reading

- [Coercion & Duress overview](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/overview): how the pages of this sub-section fit
  together
- [Transaction Flows Under Duress](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/transaction-flows-under-duress): how this
  architecture behaves under pressure
- [Seed Phrase Management](https://frameworks.securityalliance.dev/wallet-security/seed-phrase-management): offline custody for the material split here
- [Secure Multisig Best Practices](https://frameworks.securityalliance.dev/wallet-security/secure-multisig-best-practices): signer and threshold design


# Personal and Family Safety

> **KEY TAKEAWAY.** Opsec reduces what adversaries can learn about targets and routines. Controls span digital
> hygiene, identity separation between public and asset-control personas, family and staff training, physical routine
> hardening, and social engineering resistance.

Opsec shrinks the real-world attack surface by reducing what adversaries can learn about targets, their routines, and
their connections to digital assets.

## Digital hygiene

- **Eliminate persistent OSINT signals:** Scrub public profiles of home addresses, vehicle plates, routine locations
  (gyms, cafés), and geo-tagged photos. Use temporary numbers and emails for non-essential accounts. Complete PII
  removal often requires a corporate or legal entity as a shield. Run a tabletop threat model first to gauge what
  exposure is acceptable for your risk profile.
- **Harden devices:** Full-disk encryption, no seed phrases or wallet apps on always-on phones or laptops, regular
  factory resets on operational devices, no cloud sync of sensitive data.
- **Financial anonymity:** Route crypto operations through privacy-preserving tools where legally permissible, avoid
  linking exchange KYC to public social handles, use business entities for high-value holdings.

## Identity separation

- **Public persona vs. asset control:** Maintain distinct digital identities for social presence versus wallet signing.
- **Compartmentalized devices:** Public phone for social and travel use; signer phone kept in secure location, never
  carried together.
- **Family dissociation:** No joint public profiles, separate finances and devices, educate on not discussing crypto
  holdings or signing routines at home or social events.

## Physical security

- **Key storage:** Never keep cold-storage signing keys on your person or in a location that follows your physical
  routine. Store hardware wallets and seed backups in geographically separate secure locations.

## Family and staff training

- **Simple family protocols:** "If someone asks about money or crypto, say nothing and text [safe word] to [emergency
  contact]." Pre-rehearsed silent alarms to neighbors or security.
- **Staff NDAs and drills:** Drivers and assistants trained to vary routes, report surveillance, and never discuss the
  principal's assets or locations. Tabletop exercises for home and office scenarios.
- **Children and vulnerable contacts:** Age-appropriate rules ("never open the door for strangers," "never share phone
  screens"), school pick-up codes, and emergency family assembly points.
- **Panic buttons:** Fit home and vehicles with discrete panic buttons linked to a monitoring service so any household
  member can trigger a silent alert.

## Physical routine hardening

- **Unpredictability:** Rotate gyms, cafés, and commutes weekly; avoid solo night outings; use ride-shares with fake
  names or pickup locations; never carry more than $2k cash or cards visibly.
- **Home defenses:** Reinforced doors and windows, cameras with remote alerts, safe rooms, no visible luxury goods or
  crypto-branded items.
- **Travel hardening:** No wallet signing during trips, inform trusted contacts of itineraries, use hotel safes for
  devices, avoid high-profile events solo.

## Social engineering resistance

- **Standard responses to probes:** "I don't handle that" or "Ask my lawyer/colleagues" for any crypto questions. Never
  confirm or deny holdings.
- **Cover narratives:** Plausible stories like "Everything's in custody" or "The team handles treasury," consistent
  across family and staff, to deflect without raising suspicion.
- **Regular audits:** Quarterly review of social profiles, on-chain links to identities, and staff access by external
  security consultants.

## Further reading

- [Coercion & Duress overview](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/overview): how the pages of this sub-section fit
  together
- [Risk Factors and Early Signals](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/risk-factors-and-early-signals): what raises
  exposure in the first place
- [Digital Footprint](https://frameworks.securityalliance.dev/privacy/digital-footprint): reducing the public data that enables targeting
- [Data Removal Services](https://frameworks.securityalliance.dev/privacy/data-removal-services): removing address and identity records from brokers


\partpage{03}{EXTEND}{Carry protection into places, surveillance, and hardware provenance.}


# Facility & Perimeter Security

> **DOMAIN STATUS: IN PROGRESS.** The online framework currently defines scope only; this edition does not invent controls beyond the reviewed source.

> **KEY TAKEAWAY.** Facility and perimeter security protects the locations where keys, backups, and signing devices
> live through layered access control, surveillance, environmental hardening, and secure room design.

This sub-section of the [Physical Security](https://frameworks.securityalliance.dev/physical-security/overview) framework will cover
the controls that protect physical locations used for key storage and signing operations.

Planned topics include:

- Layered access control (mechanical and electronic) for homes, offices, and data rooms
- Surveillance and intrusion detection
- Environmental controls (fire, flood, power, and climate) for backup and device storage
- Secure room and safe design for high-value key material

Contributions are welcome. See the [contributing guide](https://frameworks.securityalliance.dev/contribute/contributing) to help expand this section.

## Further reading

- [Physical Security overview](https://frameworks.securityalliance.dev/physical-security/overview): how the pages of this framework fit together
- [Secure Workspace and Travel](https://frameworks.securityalliance.dev/opsec/control-domains/physical-environmental/secure-workspace-travel): existing
  guidance on workspace hardening
- [Coercion & Duress](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/overview): the most developed sub-section of this framework
- [Contributing guide](https://frameworks.securityalliance.dev/contribute/contributing): how to help expand this section


# Physical Counter-Surveillance

> **DOMAIN STATUS: IN PROGRESS.** The online framework currently defines scope only; this edition does not invent controls beyond the reviewed source.

> **KEY TAKEAWAY.** Targeted physical attacks are usually preceded by surveillance and reconnaissance. Detecting that
> activity early gives a target time to change patterns, escalate protection, or avoid an incident entirely.

This sub-section of the [Physical Security](https://frameworks.securityalliance.dev/physical-security/overview) framework will cover
how to detect and respond to physical surveillance directed at people and locations.

Planned topics include:

- Recognizing fixed and mobile surveillance
- Surveillance detection routes and pattern variation
- Identifying pre-attack reconnaissance signals
- Practical countermeasures and escalation thresholds

Contributions are welcome. See the [contributing guide](https://frameworks.securityalliance.dev/contribute/contributing) to help expand this section.

## Further reading

- [Physical Security overview](https://frameworks.securityalliance.dev/physical-security/overview): how the pages of this framework fit together
- [Risk Factors and Early Signals](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/risk-factors-and-early-signals): pre-incident
  indicators covered today
- [Digital Footprint](https://frameworks.securityalliance.dev/privacy/digital-footprint): the online half of reconnaissance
- [Contributing guide](https://frameworks.securityalliance.dev/contribute/contributing): how to help expand this section


# Supply Chain Physical Integrity

> **DOMAIN STATUS: IN PROGRESS.** The online framework currently defines scope only; this edition does not invent controls beyond the reviewed source.

> **KEY TAKEAWAY.** Hardware that custodies keys can be compromised before it reaches the user through interdiction,
> substitution, or tampering. Verifying physical provenance and tamper evidence protects the root of trust.

This sub-section of the [Physical Security](https://frameworks.securityalliance.dev/physical-security/overview) framework will cover
the physical integrity of the hardware supply chain for devices that custody keys.

Planned topics include:

- Tamper-evident packaging and seal verification
- Provenance and authenticity checks for hardware wallets and signing devices
- Detecting interdiction and device substitution
- Secure procurement and chain-of-custody practices

Contributions are welcome. See the [contributing guide](https://frameworks.securityalliance.dev/contribute/contributing) to help expand this section.

## Further reading

- [Physical Security overview](https://frameworks.securityalliance.dev/physical-security/overview): how the pages of this framework fit together
- [Tamper Evidence](https://frameworks.securityalliance.dev/opsec/control-domains/physical-environmental/tamper-evidence): existing guidance on seals and
  detection
- [Supply Chain Security](https://frameworks.securityalliance.dev/supply-chain/overview): the software and vendor counterpart
- [Contributing guide](https://frameworks.securityalliance.dev/contribute/contributing): how to help expand this section


\partpage{04}{RESPOND}{Protect life first; contain the technical surface when safe.}


# Transaction Flows Under Duress

> **KEY TAKEAWAY.** Hard limits, time delays, separation of approval channels, plausible compliance paths, and tighter
> controls during high-risk periods ensure that coerced transactions cannot drain reserves or escalate to
> higher-privilege actions.

## Hard limits and friction

- Enforce per-transaction limits and daily limits on hot and warm wallets so coerced actions cannot drain strategic
  reserves in one sitting.
- Require additional approvals once a transfer crosses predefined thresholds, even if the request looks operationally
  normal. Route approval requests across multiple independent communication channels so that a single compromised
  account cannot unilaterally authorize a transfer.
- Prefer time delays for larger movements so that an attacker must sustain control for longer, increasing the chance of
  interruption.

## Separation of approval channels

- Ensure the request and approval path are on different devices and ideally different people, so coercing one operator
  does not complete the full flow.
- Keep high-privilege signing devices physically separated from day-to-day devices used in public or during travel.
- Use geographic diversity for signers so a local incident cannot immediately compel all required approvals.

## Duress-compatible operating modes

- Maintain a plausible, low-value compliance path that can satisfy an attacker quickly without exposing core funds.
- Keep that compliance path consistent with the target's profile and normal activity so it can withstand basic scrutiny
  during coercion.
- Ensure the compliance path has no direct upgrade route to higher tiers.

## High-risk period tightening

- During travel, temporarily lower limits and increase required approvals by policy.
- Treat credible threats, doxxing, or surveillance indicators as triggers to move operations into a heightened security
  mode with reduced transaction capability.

## Further reading

- [Coercion & Duress overview](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/overview): how the pages of this sub-section fit
  together
- [Wallet and Key Architecture](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/wallet-and-key-architecture): the custody split
  these flows depend on
- [Secure Multisig Best Practices](https://frameworks.securityalliance.dev/wallet-security/secure-multisig-best-practices): thresholds and signer separation
- [Multisig for Protocols](https://frameworks.securityalliance.dev/multisig-for-protocols/overview): timelocks and approval paths at organization scale


# Incident Response

> **KEY TAKEAWAY.** During an active wrench attack, prioritize human safety first, then contain the technical surface:
> rotate signers, pause contracts where possible, coordinate with custodians and law enforcement, and preserve evidence
> for investigation.

Wrench-attack incident response must prioritize human safety first, while rapidly containing any ability to move funds
or coerce additional signers.

## Immediate triage

- Treat it as a life-safety emergency first, and assume the victim may still be under observation or ongoing coercion.
- Activate a pre-defined crisis channel and a single incident commander to avoid fragmented decisions and conflicting
  instructions. If the victim has K&R (kidnap and ransom) insurance, immediately contact their team for assistance;
  reputable firms retain hostage negotiators for these situations.
- Make an initial determination of what the attacker likely obtained.

## De-escalation

- Do not instruct actions that could escalate violence while the victim is under direct threat.
- Move the victim (and family, if relevant) to a safe location and coordinate medical care, then transition to
  controlled debriefing once stable.
- If travel-related, assume device seizure or border detention dynamics and involve local legal support immediately.

## Technical containment

- Rotate signers, disable compromised signers, and migrate funds from exposed tiers to contingency wallets.
- If smart contracts are in scope, consider pausing, timelocking, or restricting privileged functions to prevent
  coercion-driven upgrades or admin actions.
- Assume all secrets on any unlocked device are compromised, and rebuild from clean hardware with new credentials.

## Coordination with external parties

- Contact custodians, exchanges, and key infrastructure vendors via established escalation paths to block suspicious
  movements and document actions taken.
- Engage law enforcement through counsel and crisis-management support to preserve victim safety and handle reporting in
  a way that does not increase risk.
- If insurance is relevant, notify per policy requirements while controlling operational details that could leak
  sensitive signer or location information.

## Evidence and decision logging

- Preserve transaction hashes, timestamps, communications, and device state information to support investigations and
  recovery actions.
- Maintain a secure incident log of decisions, approvals, and containment steps to enable post-incident audit and
  prevent confusion across teams.
- Limit internal distribution of sensitive incident details to a strict need-to-know group to reduce secondary leakage
  and follow-on targeting.

## Post-incident actions

- Conduct a controlled post-mortem that covers both wallet architecture weaknesses and physical/OSINT exposure, then
  implement prioritized remediation.
- Refresh the entire key-management posture: new signer sets, revised limits, updated travel rules, and retraining for
  high-risk roles.
- Provide structured support for affected individuals (time off, security upgrades, relocation support when necessary)
  to reduce further harm and stabilize operations.

## Further reading

- [Coercion & Duress overview](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/overview): how the pages of this sub-section fit
  together
- [Recovery and Resilience](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/recovery-and-resilience): what follows once the
  immediate threat ends
- [Transaction Flows Under Duress](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/transaction-flows-under-duress): the limits
  that buy time during an incident
- [Incident Management](https://frameworks.securityalliance.dev/incident-management/overview): the wider response process this plugs into


\partpage{05}{RECOVER}{Rebuild trust, support people, and harden the system.}


# Recovery and Resilience

> **KEY TAKEAWAY.** Recovery rebuilds trust in wallet infrastructure and supports affected people. Reconstruction
> never reuses exposed keys, governance closes exploited gaps, and long-term monitoring detects persistent surveillance
> or follow-on attempts targeting victims and replacement wallets.

Recovery focuses on safely restoring trust in the wallet infrastructure and supporting the people affected. Resilience
means learning from the event to harden the entire system against future coercion attempts.

## Human factors

- Provide psychological support and professional counseling for victims and their families.
- Assess whether the targeted individual can realistically continue in a key-holding role given their heightened profile
  and potential ongoing risk.
- Address broader team morale and fear by communicating clearly about new security measures and support resources.

## Infrastructure reconstruction

- Do not reuse any seed phrases, private keys, or devices that were physically accessible during the incident, even if
  they appear untouched.
- Build a new wallet hierarchy from scratch and migrate remaining assets only after validating the new setup.
- Re-verify all multisig participants, threshold settings, and allowlists to ensure no attacker-controlled addresses or
  signers were inserted during the compromise.

## Governance

- Revise travel, remote-work, and high-value transaction policies to close specific gaps exploited in the attack.
- Formalize "lessons learned" into the risk register and training materials so new team members understand why specific
  constraints exist.

## Long-term monitoring

- Implement enhanced monitoring for the affected individuals and new wallet addresses to detect any persistent
  surveillance or follow-on attempts.
- Periodically re-assess the threat landscape to ensure the recovered posture remains effective over time.
- Maintain a relationship with threat intelligence and physical security partners to stay ahead of evolving coercion
  techniques targeting the sector.

## Further reading

- [Coercion & Duress overview](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/overview): how the pages of this sub-section fit
  together
- [Incident Response](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/incident-response): the phase immediately before recovery
- [Wallet and Key Architecture](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/wallet-and-key-architecture): rebuilding custody
  after compromise
- [Lessons Learned](https://frameworks.securityalliance.dev/incident-management/lessons-learned): converting the incident into durable change


# Checklist

> **KEY TAKEAWAY.** Use phased actions - immediate personal and org hardening, structural wallet and role changes
> within months, then advanced drills and monitoring - so coercion defenses mature on a clear timeline rather than ad
> hoc.

This checklist translates this section's guidance into concrete actions, divided by implementation phase and entity
type, to help prioritize deployment.

## Maturity assessment

- **Basic (high risk):** Single-factor cold storage, no daily limits, ad-hoc signing, high public visibility.
- **Intermediate (medium risk):** Multisig or MPC for treasury, basic limits, separate signing devices, some staff
  training.
- **Advanced (low risk):** Geo-distributed keys, strict role separation, time-locked reserves, regular drills, 24/7
  monitoring.

## Immediate hardening (day 1-7)

### Individual

- ( ) Remove all wallet apps, exchange account apps, seeds, and screenshots from daily-driver phones and laptops.
- ( ) Set strict daily spending limits on hot wallets (under $10k equivalent) and move excess to cold storage.
- ( ) Create one small "give-up" wallet with a realistic balance you can surrender truthfully under duress, and wire its
  duress PIN to a silent alert.
- ( ) Audit home and office for visible hardware wallets or recovery sheets and move them to secure storage.

### Organization

- ( ) Audit all active signers.
- ( ) Verify that no single person can unilaterally move more than 1-5% of treasury assets without a second approver.
- ( ) Brief key staff on "safety first" protocols.

## Structural architecture (month 1-3)

### Individual

- ( ) Separate "public identity" digital footprint from "asset control" identity:
  - ( ) Dedicated email
  - ( ) Dedicated SIM and phone
  - ( ) Dedicated device
- ( ) Establish a cold storage tier (multisig or MPC) where keys are geographically separated.
- ( ) Implement a "duress code" or panic protocol with a trusted contact or security service:
  - ( ) Trusted contact
  - ( ) Security service

### Organization

- ( ) Deploy a tiered wallet architecture (hot, warm, cold) with automated limits and a defined purpose per tier.
- ( ) Implement MPC or multisig with geographic and role-based distribution (e.g., Legal + Finance + Ops).
- ( ) Formalize the "key ceremony" process for generating and backing up new operational keys.
- ( ) Integrate wallet security training into onboarding for all staff.

## Advanced resilience (month 3-6+)

### Individual

- ( ) Conduct a full OSINT cleanup of personal data:
  - ( ) Home address
  - ( ) Family details
  - ( ) Travel patterns
  - ( ) Social media
- ( ) Establish a relationship with a physical security provider for travel risk assessments and monitoring.
- ( ) Set up a formal legal structure (trust or LLC) to obscure asset ownership where possible.
- ( ) Evaluate K&R (kidnap and ransom) insurance with a policy that covers crypto-specific risks; these providers
  typically include hostage negotiators and can advise on travel risk assessments.

### Organization

- ( ) Run quarterly tabletop exercises simulating coercion, kidnapping, and insider threats.
- ( ) Implement real-time transaction monitoring and anomaly detection for treasury wallets.
- ( ) Establish a retained incident response relationship with crypto-specialized investigators and negotiators.
- ( ) Conduct third-party penetration tests targeting technical infrastructure.
- ( ) Conduct third-party penetration tests targeting staff social engineering resistance.

## Further reading

- [Coercion & Duress overview](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/overview): how the pages of this sub-section fit
  together
- [Defensive Design Principles](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/defensive-design-principles): the reasoning
  behind these controls
- [Wallet and Key Architecture](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/wallet-and-key-architecture): the custody design
  the structural items assume
- [Personal and Family Safety](https://frameworks.securityalliance.dev/physical-security/coercion-and-duress/personal-and-family-safety): the individual
  habits behind the day 1-7 items
