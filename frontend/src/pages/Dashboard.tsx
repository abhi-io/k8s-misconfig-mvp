import { Grid, Card, CardContent, Typography, Box } from "@mui/material";

function StatCard({ title, value }: { title: string; value: string }) {
  return (
    <Card sx={{ height: "100%" }}>
      <CardContent>
        <Typography variant="body2" color="text.secondary">
          {title}
        </Typography>
        <Typography variant="h4" fontWeight={700}>
          {value}
        </Typography>
      </CardContent>
    </Card>
  );
}

export default function Dashboard() {
  return (
    <>
      <Typography variant="h5" fontWeight={700} mb={3}>
        Overview
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12} md={4}>
          <StatCard title="Customers" value="1,248" />
        </Grid>
        <Grid item xs={12} md={4}>
          <StatCard title="Orders" value="42,560" />
        </Grid>
        <Grid item xs={12} md={4}>
          <StatCard title="Alerts" value="7" />
        </Grid>

        <Grid item xs={12}>
          <Card>
            <CardContent>
              <Typography variant="h6">System Health</Typography>
              <Box mt={2} height={120} bgcolor="#0F0F14" borderRadius={2} />
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </>
  );
}
