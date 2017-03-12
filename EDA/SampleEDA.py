x=loadtxt('SampleEDA.txt')
plot((x[5000:30000,-1]/1024.*3.3-0.259388)/0.2,'k')
ylim([0,10])
ylabel('uS')
xlabel('t (ms)')
savefig('SampleEDA.png',dpi=300)
