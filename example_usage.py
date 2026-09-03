from client import PredictiveLtvChurnReengagementTriggerClient

def main():
    client = PredictiveLtvChurnReengagementTriggerClient()
    res = client.evaluate_churn_risk_and_trigger('cust_01', 30, 4, 85.00)
    print('Predictive LTV Churn Trigger: ' + res['reengagement_job_id'] + ' (' + res['churn_risk_tier'] + ')')
    print('Churn Prob: ' + str(res['churn_probability_score'] * 100) + '% | Action: ' + res['triggered_action'])
    print('Workflow URL: ' + res['campaign_workflow_url'])

if __name__ == '__main__':
    main()
