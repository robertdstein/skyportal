import * as allocationsActions from "./ducks/allocations";
import * as groupsActions from "./ducks/groups";
import * as profileActions from "./ducks/profile";
import * as sysInfoActions from "./ducks/sysInfo";
import * as dbInfoActions from "./ducks/dbInfo";
import * as earthquakeActions from "./ducks/earthquake";
import * as configActions from "./ducks/config";
import * as defaultFollowupRequestsActions from "./ducks/default_followup_requests";
import * as defaultObservationPlansActions from "./ducks/default_observation_plans";
import * as defaultSurveyEfficienciesActions from "./ducks/default_survey_efficiencies";
import * as newsFeedActions from "./ducks/newsFeed";
import * as topSourcesActions from "./ducks/topSources";
import * as recentSourcesActions from "./ducks/recentSources";
import * as mmadetectorActions from "./ducks/mmadetector";
import * as observationPlansActions from "./ducks/observationPlans";
import * as instrumentsActions from "./ducks/instruments";
import * as sourceCountsActions from "./ducks/sourceCounts";
import * as observingRunsActions from "./ducks/observingRuns";
import * as telescopesActions from "./ducks/telescopes";
import * as taxonomyActions from "./ducks/taxonomies";
import * as favoritesActions from "./ducks/favorites";
import * as rejectedActions from "./ducks/rejected_candidates";
import * as tnsrobotsActions from "./ducks/tnsrobots";
import * as enumTypesActions from "./ducks/enum_types";

export default function hydrate() {
  return (dispatch) => {
    dispatch(sysInfoActions.fetchSystemInfo());
    dispatch(dbInfoActions.fetchDBInfo());
    dispatch(configActions.fetchConfig());
    dispatch(earthquakeActions.fetchEarthquakes());
    dispatch(profileActions.fetchUserProfile());
    dispatch(groupsActions.fetchGroups(true));
    dispatch(mmadetectorActions.fetchMMADetectors());
    dispatch(newsFeedActions.fetchNewsFeed());
    dispatch(topSourcesActions.fetchTopSources());
    dispatch(instrumentsActions.fetchInstruments());
    dispatch(allocationsActions.fetchAllocations());
    dispatch(instrumentsActions.fetchInstrumentForms());
    dispatch(recentSourcesActions.fetchRecentSources());
    dispatch(sourceCountsActions.fetchSourceCounts());
    dispatch(observingRunsActions.fetchObservingRuns());
    dispatch(telescopesActions.fetchTelescopes());
    dispatch(taxonomyActions.fetchTaxonomies());
    dispatch(favoritesActions.fetchFavorites());
    dispatch(rejectedActions.fetchRejected());
    dispatch(tnsrobotsActions.fetchTNSRobots());
    dispatch(enumTypesActions.fetchEnumTypes());
    dispatch(observationPlansActions.fetchObservationPlanNames());
    dispatch(defaultFollowupRequestsActions.fetchDefaultFollowupRequests());
    dispatch(defaultObservationPlansActions.fetchDefaultObservationPlans());
    dispatch(defaultSurveyEfficienciesActions.fetchDefaultSurveyEfficiencies());
  };
}
