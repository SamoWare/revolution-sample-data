x=loadtxt('SamplePZT.txt')
plot(x[5000:30000,-1]/4096*100-50,'k')
ylim([-50,50])
ylabel('%')
xlabel('t (ms)')
savefig('SamplePZT.png',dpi=300)
