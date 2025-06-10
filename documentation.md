# PersonalTokenNet

## Getting Started

### What is a personal token?

Your personal token is an instrument that represents your equities in companies and other personal tokens.
![\2](\1)
Personal tokens exist within a network (the "Net"). Every user, whether they want to raise capital, or invest in other personal tokens, will need to create their personal token.
When you first create your personal token, it's divided into 10 million shares - which you own all of. When you raise capital, you issue new shares to investors who become your personal token "shareholders".
Your personal token contains information about who you are, your token shareholders, and history of transactions: fundraising events, assets (equities in companies and other personal tokens) and investment history.
You can only have one personal token on the network. You can't delete an existing personal token to create a new one.
A personal token is associated with a wallet that holds [USDC](https://www.notion.so/docs-1f97eb80e06c800a84e8e4bf40fc04c9?pvs=21). This wallet is where funds are deposited when you successfully raise capital by selling shares of your personal token, and where funds are withdrawn from to facilitate investments you make in other personal tokens.

---

### Create your personal token

During the onboarding you'll receive a link to verify your identity by submitting a government issued ID and a selfie photo.
Once your identity is verified, you'll be issued a personal token and will be able to start transacting on the Net.
You can only have one personal token on the Net.

---

## Fundraise

### Overview

You can raise capital by selling shares of your personal token through discrete fundraising "rounds."
When you initiate a round, you specify the terms of your offering: how many shares you want to sell and at what price per share. This establishes your token's valuation and determines how much ownership percentage you're transferring to investors. For example, selling 1 million shares (10% of your token) at $1 per share values your entire token at $10 million.
You can share a link to your active round with prospective investors, who can then indicate their interest and proposed investment amount. You maintain complete control over investor selection, allowing you to curate your cap table strategically. Each investor you accept will receive shares proportional to their investment, becoming shareholders.
When you complete the round, the investment funds are immediately deposited into your personal token wallet, and the Network automatically updates all ownership records to reflect the new distribution of shares.

---

### Dilution

With each funding round, ownership percentages shift as new shares are issued. Your original shareholders (including yourself) will experience some degree of ownership dilution as the total number of outstanding shares increases.
Dilution is when the percentage ownership of existing shareholders, including the token owner, decreases when the token owner issues new shares during a fundraising round.
For example: let's say your personal token has 10 million total shares, and you own 9 million (90%) after an initial fundraising round where investors purchased 1 million shares (10%). If you decide to raise more capital by selling an additional 1 million new shares, the total share count increases to 11 million. After this second round, you would own 9 million out of 11 million shares (approximately 81.8%), while your initial investors would own 1 million out of 11 million (approximately 9.1%). T
To create alignment with early investors who take the highest risk, personal tokens incorporate certain protections borrowed from traditional equity structures:1
1. **Pro rata rights**: existing shareholders have the right (but not obligation) to participate in future funding rounds to maintain their ownership percentage. This gives early believers in your potential the opportunity to continue supporting your journey without being diluted.
2. **Information rights**: shareholders must receive notice of an upcoming fundraising round at least a week in advance so that they have time to exercise their pro rata rights.
3. **Anti-dilution provisions**: if you raise capital at a valuation lower than previous rounds (a "down round"), the Network will automatically adjust share allocations to protect early investors from severe dilution, similar to [weighted-average anti-dilution provisions](https://www.andrew.cmu.edu/user/fd0n/53%20Weighted%20Average%20Anti-dilution.htm) in traditional venture financing.
---

---

### Start Fundraising Round

[This section is currently empty]

---

### Invite Investors

[This section is currently empty]

---

### Open Round To Net

[This section is currently empty]

---

### Manage Round

[This section is currently empty]

---

### Withdraw Capital

[This section is currently empty]

---

## Invest

### Overview

You can invest in personal tokens _through_ your personal token.
In order to accept an invitation from a user to invest, you must have sufficient capital in your personal token wallet to cover the investment amount.
There are 2 ways to profit from investing:
1. [Dividends](/docs/dividends)
2. Selling shares to another investor (or back to the token owner) at a higher price than you bought them for ([secondary sales](/docs/secondary-sales)).

---

### Deposit Capital

[This section is currently empty]

---

### Secondary Sales

When a shareholder wants to sell their equity in a personal token, they initiate a "Secondary Sale Request" in the Network. This request specifies the number of shares they wish to sell, their asking price, and how long the offer remains valid. Similar to private companies' [Right of First Refusal](https://www.angellist.com/learn/right-of-first-refusal) (ROFR), the token holder gets the first opportunity to purchase these shares. This ensures token holders maintain influence over their cap table and prevents unwanted parties from acquiring shares. If the token holder declines to purchase the shares, other existing shareholders receive second priority to maintain alignment among current investors.
The ROFR period lasts 14 days for the token holder and an additional 7 days for existing shareholders. If no existing shareholders purchase the shares during this period, the seller can either list their shares on the Network's internal marketplace or have someone they know apply to invest. All transfers must be approved by the token holder, and shares can only be transferred to other verified users in the Network.
For each completed secondary sale, a small [royalty fee](/fees#secondary-sale-transaction-fee) is charged.

---

## Other

### Secondary sale transaction fee

A royalty fee of (2%) is automatically collected from the transaction value. This fee is split between the token owner (1.5%) and the Network (0.5%). This royalty structure creates an incentive for token owners to approve secondary sales, providing liquidity for early investors while generating ongoing returns for token owners as their personal token gains popularity in the secondary market.
For example: an investor purchased 100,000 shares of your personal token at 2 USD per share (200,000 USD total) during your fundraising round three years ago. Now, they wish to sell 50,000 shares at 5 USD per share (250,000 USD total) through a Secondary Sale Request. If you exercise your right of first refusal, you would pay 250,000 USD to reacquire these shares. If you decline, your existing shareholders have 7 days to purchase these shares. Assuming the sale completes at the 5 USD price, a 2% fee (5,000 USD) would be charged, with 3,750 USD (1.5%) going to you as the token owner and 1,250 USD (0.5%) going to the Network. The seller would receive 245,000 USD, and the buyer would receive 50,000 shares.
### Equity fee
Every time an individual raises funds through their personal token on the Net, a modest fraction of newly issued shares—just 0.1%—is automatically allocated to the [Network Token](/network-token). In practice, this means the Network Token continuously accumulates micro-stakes across the entire ecosystem of personal tokens.

---

### Tax

[This section is currently empty]

---

### Dividends

If you have shareholders in your personal token, whenever you sell equity in a personal token or a company at a profit, the capital gains (the profit portion, not the entire proceeds) from that sale are distributed to those who hold equity in your personal token - proportional to how much equity they hold.
For example, if you purchased personal token or company shares for 10,000 USD and later sold them for 15,000 USD, the 5,000 USD profit would be distributed to your personal token shareholders according to their ownership percentages.
Capital gains distributions flow directly to the holders of the seller's personal token, but do not cascade further up the network. For example, if Alice holds shares of Bob's personal token, and Bob holds shares of Dan's personal token, then when Dan sells equity and generates capital gains, these gains are distributed proportionally to Dan's token holders (including Bob) but stop there - they do not automatically flow up to Bob's token holders (like Alice). Alice can only benefit from Dan's success indirectly if Bob's token value increases due to his gains from Dan, and Alice then sells her equity in Bob's token at this higher value.
Dividends are immediately paid out when you sell equity in a personal token - since that capital and information lies within the network. On the other hand, when you sell equity in a company, it's your responsibility to pay dividends for that to your shareholders through the network. You can do this on a yearly basis, by the US tax deadline.
We're building tooling to make this a very simple process for you. Any discrepancies / delays may affect your reputation in the network, which will be visible to your shareholders, future shareholders, and those you want to invest in.

---

### Reporting Capital Gains

If you have shareholders, when you sell equity in companies, since they exist outside of the Network, it's your responsibility to report these transactions and distribute the appropriate capital gains to your shareholders. If you don't have shareholders there's no need to report.
You are required to report your equity sales once a year, before the tax deadline. You'll provide basic information about what you sold, when you sold it, your original purchase price, and the sale price.
Most users can complete this annual reporting in minutes through our simple interface. We're actively building integrations with popular equity management platforms and investment services, which will allow many of your transactions to be imported automatically when these integrations launch. For transactions not covered by these integrations, you'll upload standard documents you're already preparing for taxes, like transaction records or tax forms. Our system calculates the capital gains and processes the actual distribution to your shareholders. If your personal token wallet doesn't have sufficient capital, you will be prompted to deposit the necessary funds.
The Network maintains a reputation system that tracks your reporting history and accuracy. Consistent, timely reporting enhances your reputation score, which is visible to current and potential investors. Significant discrepancies or delays in reporting may affect this score. For larger transactions, a small percentage of distributed funds may be temporarily held in escrow until verification is complete.
We're going to make this process as simple and automated as possible. We'll be there by your side to minimize admin BS.

---

### The Net

The Net is the protocol itself — a set of open, on-chain contracts that mint personal tokens, record every fundraising or secondary sale, and route the 0.10 % “equity fee” (plus any secondary-sale royalties) into a single treasury.
Nobody owns the Net outright. It's a public-good financial rail to facilitate creating personal tokens and transacting personal token equities.

---

### The Company (CCorp)

The C-Corp is the Delaware company that: owns the flagship web/mobile front-end and trademarks, will carry the U.S. broker-dealer / ATS licences that make personal-token trading legal for retail users, employs the engineers and absorbs early compliance costs.
In other words, the C-Corp is the first (eventually not the only) operator that connects people to the Net.

---

### Network Token

At its heart, the Network Token is an index on the potential of every citizen of the Net, by capturing a tiny fraction of every personal token that successfully raises capital. Owning shares in the Network Token is a bet on the collective potential of everyone in the Net.
### How does the Network Token capture value?
Every time an individual raises funds through their personal token on the Net, a modest fraction of newly issued shares—just 0.1%—is automatically allocated to the Network Token treasury. In practice, this means the Network Token continuously accumulates micro-stakes across the entire ecosystem of personal tokens.
### Supply, allocation, and decentralization
To preserve fairness and stability, the Network Token is minted just once, with a capped total supply of 100 million tokens. At launch, only a limited portion (20%) is immediately available. This initial distribution covers early contributors, the founding team, early investors, liquidity providers, and community incentives.
- **20% Team & Early Contributors**: Tokens allocated to the founding team and early supporters vest gradually over four years, with a standard one-year cliff—aligning incentives with long-term project health.
- **50% Protocol Treasury**: Reserved for ecosystem development, grants, liquidity incentives, and future community-driven initiatives. These tokens unlock incrementally over several years, guided by community governance.
- **15% Early Investors**: Allocated to seed and early investors in the form of token warrants, vesting alongside the team to prevent rapid sell-offs.
- **10% Public Sales and Future Community Distribution**: Held back for future regulated token sales (Reg CF, Reg D) to invite broader community participation, progressively decentralizing ownership.
- **5% Liquidity and Market-making**: Provided upfront to ensure healthy trading liquidity and market stability.
### Dividends
Unlike personal tokens, the Network Token does not provide dividends to its holders as all proceeds will be used to fund the Network's operations and growth. As the Network grows and reaches sufficient scale and maturity, a growing percentage of the Network's capital gains will be distributed to Network Token holders.

---

### Reputation

[This section is currently empty]

---

### Legal

[This section is currently empty]

---

## Frequently asked

### Why dilution?

Dilutive issuance maximizes deployable capital, minimizes tax drag, and signals long-term commitment to every new investor.

---

### Shareholders voting rights?

Absolutely not.
Personal token shareholders can't vote on anything, and have no direct say in the actions of the personal token owner. A shareholder is simply a participant on the sidelines of the journey of the personal token owner.

---
