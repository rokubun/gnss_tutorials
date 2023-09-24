# Rate ot TEC Index (ROTI)

The ROTI, as proxy for a measure of scintillation, was introduced in {cite:p}`pi2013observations`, and basically consists in computing the standard deviation of the rate of TEC over a certain time interval. It can be easily computed using the ionospheric (geometry-free) combination of GNSS carrier phase measurements. In short, the steps to compute it are described in {prf:ref}`roti`.

```{prf:algorithm} Satellite ROTI calculation
:label: roti
:nonumber:

**Inputs** Carrier-phase GNSS measurements at two bands (e.g. L1 and L2)

**Output** Time series of ROTI (TECU/minute)

1. For each GNSS satellite

    1. Compute the ionospheric (geometry) free combination of carrier phases at frequencies $f_1$ and $f_2$: $LI = L1 - L2$
    2. Compute the time difference of $LI$: $\Delta LI = \frac{\delta LI}{\delta t}$
    3. Compute the time difference of $STEC$: $\Delta STEC = \Delta LI / \alpha_{LI}$,
        where $\alpha_{LI} = 40.3 \cdot (\frac{1}{f_2^2} - \frac{1}{f_1^2})$
    4. Compute the standard deviation of the $\Delta STEC$ across consecutive time intervals of e.g. 5 minutes
```

An example of the ROTI calculation for a 1Hz dataset of SEY1 station (2014, doy 58) can be found in {cite:p}`juan2017method`

![Juan et al. 2017 Figure 2b](../assets/juanetal2017_fig2b_roti_sey1.png)

In this recipe we will replicate this figure (for the SEY1 station) using the methodology described in {prf:ref}`roti`
