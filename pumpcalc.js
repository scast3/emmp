
function power(q, h, n, t) {
    const powerhp = (q*h)/(3960*(n/100));
    const kwh = powerhp * 0.7456;

    const energy = kwh*t
    return energy;
}

function powerdif(flow1, head1, efficiency1, flow2, head2, efficiency2) {
    // Calculate power for Pump 1
    const power1 = power(flow1, head1, efficiency1);

    // Calculate power for Pump 2
    const power2 = power(flow2, head2, efficiency2);

    // Calculate the difference in power
    const powerDifference = power2 - power1;

    return powerDifference;
}



