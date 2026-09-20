# OpRa Part 8 Class Extraction

**Extraction Date:** 2026-05-14
**Model File:** TransmodelEcoSystem2024-EAv16-nk84_OpRa-v13.qea
**Total Packages:** 26
**Total Classes:** 67

## Package Tree
```
{
  "Part 8 - Management Information & Statistics (MI)": {
    "RC Reusable Components MODELs": {
      "RC Reusable Components MODELs": {
        "LT Logging Time and Place MODEL": {
          "LT Logging Time and Place MODEL": null
        },
        "RV Recorded Vehicle MODELs": {
          "RV Recorded Vehicle MODELs": null
        },
        "RT Recorded Trip MODEL": {
          "RT Recorded Trip MODEL": null
        },
        "FS Filtering Supoort MODELs": {
          "FS Filtering Supoort MODELs": null
        },
        "GA Generic Aggregations MODELs": {
          "GA Generic Aggregations MODELs": null
        },
        "DM Data Managed Object MODEL": {
          "DM Data Managed Object MODEL": null
        }
      }
    },
    "QM Query MODEL": {
      "QM Query MODEL": null
    },
    "EF Explicit Frame MODELs": {
      "EF Explicit Frame MODELs": {
        "RF Indicator Frame MODEL": {
          "RF Indicator Frame MODEL": null
        },
        "PF Planned Frame MODEL": {
          "PF Planned Frame MODEL": null
        },
        "AF Actual Frame MODEL": {
          "AF Actual Frame MODEL": null
        },
        "CI Contextual Indicator Frame MODEL": {
          "CI Contextual Indicator Frame MODEL": null
        }
      }
    },
    "ID Indicator MODELs": {
      "ID Indicator MODELs": {
        "CJ Cancelled Dated Vehicle Journeys MODELs": {
          "CJ Cancelled Dated Vehicle Journeys MODELs": null
        },
        "LJ Late Dated Vehicle Journeys MODELs": {
          "LJ Late Dated Vehicle Journeys MODELs": null
        },
        "PX Measured Number of Passengers MODELs": {
          "PX Measured Number of Passengers MODELs": null
        },
        "EX Expected Number of Passengers MODELs": {
          "EX Expected Number of Passengers MODELs": null
        },
        "SI Service Intensity Indicators MODELs": {
          "SI Service Intensity Indicators MODELs": null
        },
        "SD Service Dimensions Indicator MODELs": {
          "SD Service Dimensions Indicator MODELs": {
            "UC Use Cases": {
              "UC Use Cases": null
            }
          }
        },
        "FD Fleet Dimensions Indicators MODELs": {
          "FD Fleet Dimensions Indicators MODELs": {
            "UC Use Cases": {
              "UC Use Cases": null
            }
          }
        },
        "OC Offered Capacity MODELs": {
          "OC Offered Capacity MODELs": {
            "UC Use Cases": {
              "UC Use Cases": null
            }
          }
        }
      }
    }
  }
}
```

## Classes by Package

### AF Actual Frame MODEL (1 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| ACTUAL FRAME | - | ✓ | id: ActualFrameIdType | None (Generalization), None (Aggregation) |

### CI Contextual Indicator Frame MODEL (4 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| CONTEXT KEYLIST | - | ✓ | Id: ContextKeyValueIdType | None (Association), None (Aggregation) |
| CONTEXTUAL INDICATOR | - | ✓ | Id: ContextualIndicatorIdType, ContextIndicatorIdentifier: char, ContextIndicatorValue: char | None (Association), None (Association), None (Generalization) |
| CONTEXTUAL INDICATOR FRAME | - | ✓ | Id: ContextualIndicatorFrameIdType, ContextIdentifier: char, ContextVersion: char | None (Generalization), None (Aggregation), None (Association) |
| GENERIC CONTEXTUAL INDICATOR | - | ✓ | Id: GenericContextualIndicatorIdType | None (Generalization), None (Association) |

### CJ Cancelled Dated Vehicle Journeys MODELs (3 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| CANCELLED DATED VEHICLE JOURNEY COUNT | - | ✓ | Id: CancelledDatedVehicleJourneyCountIdType | None (Association), None (Generalization), calculates from (Dependency) |
| CANCELLED DATED VEHICLE JOURNEY ENTRY | - | ✓ | Id: CancelledDatedVehicleJourneyEntryIdType | None (Generalization), None (Aggregation), None (Association) |
| CANCELLED JOURNEY OCCURRENCE | - | ✓ | Id: CancelledJourneyOccurenceIdType | calculates from (Dependency), calculates for any PT context (Dependency), None (Generalization) |

### DM Data Managed Object MODEL (3 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| DATA MANAGED OBJECT | - | ✓ | KeyList: KEY LIST | None (Generalization), None (Aggregation) |
| KEY LIST | - | ✓ | KeyValue: KEY VALUE | None (Aggregation), None (Aggregation), None (Aggregation) |
| KEY VALUE | - | ✓ | Key: char, Value: char, TypeOfKey: char | None (Aggregation) |

### EX Expected Number of Passengers MODELs (2 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| EXPECTED PASSENGER COUNT | - | ✓ | id: ExpectedPassengerCountIdType, numberOfPassengers: int | None (Generalization), None (NoteLink), None (Association) |
| EXTERNAL PASSENGER COUNT | - | ✓ | id: ExternalPassengerCountIdType | None (Association), None (Generalization), None (NoteLink) |

### FD Fleet Dimensions Indicators MODELs (3 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| ACTUAL FLEET DIMENSIONS | - | ✓ | id: ActualFleetDimensionsIdType | None (Generalization) |
| FLEET DIMENSIONS | - | ✓ | NumberOfVehiclesTotal: nonNegativeInteger, NumberOfVehiclesRequired: nonNegativeInteger, NumberOfVehiclesInReserve: nonNegativeInteger | None (Generalization), None (Association), None (Association) |
| PLANNED FLEET DIMENSIONS | - | ✓ | id: PlannedFleetDimensionsIdType | None (Generalization) |

### FS Filtering Supoort MODELs (2 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| CALENDAR AWARE PT SCOPE | - | ✓ | Id: CalendarAwarePtScope | None (Association), None (Association), None (Association) |
| FLEET SCOPE | - | ✓ | Id: FleetScopeIdType | None (Association), None (Association), None (Association) |

### GA Generic Aggregations MODELs (3 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| DURATION DISTRIBUTION | - | ✓ | Id: DurationDistributionIdType, Mean: DurationType | None (Aggregation), None (Aggregation) |
| DURATION INTERVAL | - | ✓ | Id: DurationIntervalIdType, Name: char, StartIsNegative: boolean | None (Association), None (Aggregation), None (Generalization) |
| OCCURRENCE | - | ✓ | Id: OccurrenceIdType, NumberOfOccurrences: nonNegativeInteger, PercentageOfOccurrences: PercentageType | None (Aggregation), None (Generalization), None (Generalization) |

### ID Indicator MODELs (2 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| INDICATOR | - | ✓ | Id: IndicatorIdType | None (Aggregation), None (Generalization), None (Generalization) |
| INDICATOR LOG ENTRY | - | ✓ | Id: IndicatorLogEntryIdType | None (Aggregation), None (Generalization), None (Aggregation) |

### LJ Late Dated Vehicle Journeys MODELs (5 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| LATE DATED VEHICLE JOURNEY COUNT | - | ✓ | Id: LateDatedVehicleJourneyCountIdType | None (Generalization), None (NoteLink), None (Aggregation) |
| LATE DATED VEHICLE JOURNEY ENTRY | - | ✓ | id: LateDatedVehicleJourneyEntryIdType | None (Generalization), None (Association), None (Aggregation) |
| LATE JOURNEY INTERVAL | - | ✓ | Id: LateJourneyIntervalIdType | calculates for any PT context (Dependency), None (Generalization) |
| LATE JOURNEY OCCURRENCES | - | ✓ | Id: LateJourneyOccurenceIdType | None (Generalization), None (Aggregation) |
| MEAN DELAY | - | ✓ | Id: MeanDelayIdType, Delay: int | None (Association), None (Aggregation), None (NoteLink) |

### LT Logging Time and Place MODEL (1 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| LOCATED EVENT | - | ✓ | Id: LocatedEventIdType, ReceivedAt: dateTime | None (Generalization), None (Association), None (Association) |

### OC Offered Capacity MODELs (3 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| ACTUAL CAPACITY | - | ✓ | id: ActualCapacityIdType | None (Generalization), None (Association), None (Aggregation) |
| OFFERED CAPACITY | - | ✓ | OccupancyScopeFilterGroup: group | None (Association), None (Association), None (Association) |
| PLANNED CAPACITY | - | ✓ | id: PlannedCapacityIdType | None (Generalization) |

### PF Planned Frame MODEL (1 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| PLANNED FRAME | - | ✓ | id: PlannedFrameIdType | None (Generalization), None (Aggregation), None (Aggregation) |

### PX Measured Number of Passengers MODELs (6 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| AGGREGATED BOARDING AND ALIGHTING ENTRY | - | ✓ | id: AggretedBoardingAndAlightingEntryIdType | None (Aggregation), None (Generalization), None (NoteLink) |
| AGGREGATED ONBOARD DEVICE BASED PASSENGER COUNT | - | ✓ | id: AggregatedOnboardDeviceBasedPassengerCountIdType | None (Generalization), None (Aggregation), None (NoteLink) |
| AGGREGATED TICKETING BASED PASSENGER COUNT | - | ✓ | id: AggregatedTicketingBasedPassengerCountIdType | None (Generalization), None (Association), None (Aggregation) |
| BOARDING AND ALIGHTING BASED PASSENGER COUNT  | - | ✓ | id: ExternalPassengerCountIdType, numberOfPassengers: int | None (Generalization), None (Generalization), None (Association) |
| ONBOARD DEVICE BASED PASSENGER COUNT | - | ✓ | id: OnboardDeviceBasedPassengerCountIdType, numberOfPassengers: int | None (Generalization), None (Association), None (Aggregation) |
| TICKETING BASED PASSENGER COUNT | - | ✓ | id: TicketingBasedPassengerCountIdType | None (Association), None (Association), None (Generalization) |

### QM Query MODEL (6 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| AGGREGATE FUNCTION | - | ✓ | Id: MiRequestPolicyIdType, IncludeNotices: boolean, PreferredLanguage: lang | None (Aggregation) |
| AGGREGATION INSTRUCTIONS | - | ✓ | Id: MiRequestFilterIdType | None (Aggregation) |
| GROUPING INSTRUCTION | - | ✓ | Id: TypeOfRequestIdType | None (NoteLink), None (NoteLink), None (Association) |
| OPRA FUNCTIONAL DELIVERY | - | ✓ | Id: MiDeliveryIdType, StartTime: dateTime, EndTime: dateTime | None (NoteLink), None (Association), None (Association) |
| OPRA FUNCTIONAL REQUEST | - | ✓ | Id: MiRequestIdType | None (Association), None (Association), None (Association) |
| PARTICIPANT SYSTEM | - | ✓ | Id: ParticipantIdType | None (Association), None (Association), None (Association) |

### RF Indicator Frame MODEL (1 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| INDICATOR FRAME | - | ✓ | Id: IndicatorFrameIdType | None (Generalization), None (Aggregation), None (Association) |

### RT Recorded Trip MODEL (2 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| RECORDED LEG | - | ✓ | Id: RecordedLegIdType | None (Aggregation), None (Association), None (Generalization) |
| RECORDED TRIP | - | ✓ | Id: RecordedTripIdType | None (Association), None (Generalization), None (Aggregation) |

### RV Recorded Vehicle MODELs (3 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| BOARDING AND ALIGHTING | - | ✓ | Id: BoardingAndAlightingIdType, Occupancy: boolean, NumberOfAlighters: nonNegativeInteger | None (Association), None (Association), None (Generalization) |
| INTERCHANGE STATUS | - | ✓ | Id: InterchangeStatusIdType, NumberOfPassengers: nonNegativeInteger, CauseOfMissedInterchange: MultilingialString | None (Association), None (Association), None (Generalization) |
| RECORDED STOP | - | ✓ | Id: RecordedStopIdType, DoorsClosedTime: dateTime, DoorsOpenedTime: dateTime | None (Association), None (Association), None (Generalization) |

### SD Service Dimensions Indicator MODELs (3 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| ACTUAL SERVICE DIMENSIONS | - | ✓ | Id: ActualServiceDimensionsIdType | None (Generalization), None (Generalization) |
| PLANNED SERVICE DIMENSIONS | - | ✓ | Id: PlannedServiceDimensionsIdType | None (Generalization), None (NoteLink) |
| SERVICE DIMENSIONS | - | ✓ | NumberOfStopPoints: nonNegativeInteger, NumberOfLines: nonNegativeInteger, NumberOfRoutes: nonNegativeInteger | None (Aggregation), None (Generalization), None (Association) |

### SI Service Intensity Indicators MODELs (12 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| ACTUAL SERVICE INTENSITY | - | ✓ | Id: ActualServiceIntensityIdType | None (Generalization) |
| AVERAGE COMMERCIAL SPEED | - | ✓ | Id: LoadOverJourneyDistanceIdType, AverageCommercialSpeed: double | None (Association) |
| CAPACITY OVER DISTANCE | - | ✓ | Id: ÇapacityOverDistanceIdType, Distance: int | None (Association), None (Association), None (Association) |
| EXPECTED SERVICE INTENSITY | - | ✓ | Id: ExpectedServiceIntensityIdType | None (Generalization) |
| LOAD OVER JOURNEY DISTANCE | - | ✓ | Id: LoadOverJourneyDistanceIdType | None (Association), None (Association) |
| MEAN CAPACITY OVER JOURNEY DISTANCE | - | ✓ | Id: MeanCapacityOverJourneyDistanceIdType | None (Association), None (Association) |
| MEAN CAPACITY OVER NETWORK DISTANCE | - | ✓ | Id: MeanCapacityOverNetworkDistanceIdType | None (Association), None (Association) |
| MEAN CAPACITY OVER ROUTE DISTANCE | - | ✓ | Id: MeanCapacityOverRouteDistanceIdType | None (Association), None (Association) |
| PLANNED SERVICE INTENSITY | - | ✓ | Id: PlannedServiceIntensityIdType | None (Generalization) |
| SERVICE INTENSITY | - | ✓ | id: ServiceIntensityIdType | None (Generalization), None (Association), None (Association) |
| TRANSPORT PERFORMANCE | - | ✓ | Id: TransportPerformanceIdType, Distance: int | None (Association), None (Association), None (Generalization) |
| TRANSPORT PERFORMANCE PER VEHICLE | - | ✓ | Id: TransportPerformancePerVehicleIdType | None (Generalization), None (Association), None (Association) |

### UC Use Cases (1 classes)

| Class | Parent | Abstract | Key Attributes | Relationships |
|-------|--------|----------|----------------|----------------|
| VEHICLE SEAT COUNT | - | ✓ | Id: VehicleSeatCountIdType | None (Association), None (Aggregation) |
