<!-- Hãy sử dụng Ngôn ngữ chung (Ubiquitous Language) trong domain driven design (DDD) với nội dung nghiệp vụ kinh doanh sau: -->

<!-- 1. **Khách hàng (Customer):** -->
<!-- - **Mô tả:** Người sử dụng dịch vụ, có thể là cá nhân hoặc tổ chức. -->

<!-- 2. **Hóa đơn điện tử (Electronic Invoice):** -->
<!-- - **Mô tả:** Hóa đơn được tạo và quản lý điện tử thay vì truyền thống trên giấy. -->

<!-- Bằng cách sử dụng ngôn ngữ chung như trên, chúng ta có thể tạo ra một mô hình DDD rõ ràng và dễ hiểu, giúp các đội phát triển, quản lý dự án và người dùng hiểu rõ về các yêu cầu và chức năng của hệ thống. -->
<!--@  -->
<!--@  -->
<!--@  -->
<!--@  -->
<!--@  -->
<!--@  -->

Trình bày về Dual Write trong domain driven design

https://ddd-practitioners.com/home/glossary

<!--@Thiết kế hướng tên miền -->

DDD là một phương pháp thiết kế phần mềm tập trung vào việc hiểu rõ và mô hình hóa ngữ cảnh kinh doanh trong các hệ thống phần mềm.

<!-- Domain-Driven Design : https://ddd-practitioners.com/domain-driven-design   -->
<!-- Business Model Canvas : https://ddd-practitioners.com/business-value-canvas -->

có thể nêu thêm thôi

<!-- Domain : https://ddd-practitioners.com/domain   -->
<!-- Problem Domain :https://ddd-practitioners.com/home/glossary/problem-domain -->
<!-- Solution Domain :https://ddd-practitioners.com/home/glossary/solution-domain -->
<!-- subdomain: https://ddd-practitioners.com/home/glossary/subdomain-->
<!-- Core Domain   https://ddd-practitioners.com/home/glossary/domain/core-domain/   -->

Cần lưu ý rằng ý tưởng về tên miền phụ cốt lõi, hỗ trợ và chung có thể khác nhau ngay cả đối với các doanh nghiệp hoạt động trong cùng một tên miền. Điều này là do các tên miền phụ và vai trò của chúng được xác định theo nhu cầu kinh doanh và bối cảnh cụ thể của mỗi tổ chức. Ví dụ:

<!-- Generic Subdomain : https://ddd-practitioners.com/generic-subdomain -->
<!-- Supporting Subdomain : https://ddd-practitioners.com/supporting-subdomain -->

<!-- Domain Object : https://ddd-practitioners.com/domain-object   -->
<!-- Entity : https://ddd-practitioners.com/entity   -->
<!--!Value -->

<!-- Domain Model: https://ddd-practitioners.com/home/glossary/domain-model -->

<!-- Domain Services: https://ddd-practitioners.com/home/glossary/domain-services -->
<!-- Application Service : https://ddd-practitioners.com/application-service -->
<!-- Big Ball of Mud : https://ddd-practitioners.com/home/glossary/big-ball-of-mud   -->

là kết quả của thiết kế kém, mã hóa đặc biệt và thiếu tầm nhìn xa.
Loại hệ thống này khó thay đổi, hiểu và kiểm tra, đồng thời thường có thể dẫn đến

 <!-- nợ kỹ thuật -->

và các vấn đề dài hạn cho một dự án phần mềm.

<!-- CI/CD -->

<!-- Bounded Context: https://ddd-practitioners.com/home/glossary/bounded-context -->

Mỗi bounded context nên tương ứng với một nhóm hoặc bộ phận cụ thể trong tổ chức. Sự tương ứng này có thể giúp giảm thiểu sự hiểu lầm và tăng khả năng tương tác giữa các đội ngũ.

Ví dụ: khách hàng có thể có nhiều ý nghĩa khác nhau tùy thuộc vào ngữ cảnh: trong ngữ cảnh thanh toán, đó là người nợ tiền; trong bối cảnh vận chuyển, đó là người nhận hàng. Bằng cách tạo một mô hình riêng cho từng ngữ cảnh, bạn có thể tránh nhầm lẫn và làm cho mã rõ ràng hơn.

<!-- Bounded Context Relationships : https://ddd-practitioners.com/bounded-context-relationship   -->

<!-- Context Mapping : https://ddd-practitioners.com/context-map -->

Hữu ích cho việc hiểu kiến ​​trúc tổng thể

<!-- Customer/Supplier : https://ddd-practitioners.com/customer-supplier   -->

<!-- Conformist : https://ddd-practitioners.com/conformist   -->
<!-- Anti-Corruption Layer (ACL) : https://ddd-practitioners.com/anticorruption-layer -->

<!-- Aggregate:   https://ddd-practitioners.com/home/glossary/aggregate/ -->
<!-- Consistency Boundary : https://ddd-practitioners.com/glossary/consistency-boundary -->

<!--@saga -->
<!--@CQRS (Command Query Responsibility Segregation): -->
<!--@Event Sourcing: -->

Một mô hình lưu trữ dữ liệu, trong đó tất cả các thay đổi trạng thái của hệ thống được biểu diễn dưới dạng sự kiện (event).

<!-- EventStorming : https://ddd-practitioners.com/home/glossary/eventstorming   -->
<!-- Domain Storytelling : https://ddd-practitioners.com/?page_id=1005 -->

<!-- CQRS : https://ddd-practitioners.com/?page_id=574 -->

CQRS chia để thoải mái, chặt chẽ

Là một nguyên tắc trong DDD, CQRS tách biệt giữa phần xử lý câu lệnh (Command) và phần truy vấn dữ liệu (Query).
Command đại diện cho các thao tác cập nhật dữ liệu, trong khi Query đại diện cho các thao tác truy vấn dữ liệu.

<!-- Change Data Capture: https://en.wikipedia.org/wiki/CAP_theorem -->

<!-- ACID Transaction : https://ddd-practitioners.com/?page_id=415 -->

ACID (Atomicity, Consistency, Isolation, Durability)

<!-- BASE Transaction  -->

BASE là viết tắt của "Basically Available, Soft state, Eventually consistent," và đối lập với ACID

<!-- Command : https://ddd-practitioners.com/?page_id=596 -->
<!-- Command Handler : https://ddd-practitioners.com/?page_id=599 -->
<!-- Compensating Action : https://ddd-practitioners.com/compensating-action   -->
<!-- Compensating Transaction : https://ddd-practitioners.com/compensating-transaction   -->
<!-- Compensating Workflow : https://ddd-practitioners.com/compensating-workflow   -->

<!-- Domain Event : https://ddd-practitioners.com/domain-event   -->
<!-- PublishSubscribe : https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html -->
<!--@ Dependency Inversion Principle    -->
<!--!========================================================== -->
<!--!========================================================== -->
<!--!========================================================== -->
<!--!========================================================== -->
<!--!========================================================== -->
<!--!========================================================== -->
<!--!========================================================== -->
 <!-- mỗi dịch vụ xuất bản và đăng ký các sự kiện nếu cần.    Cách tiếp cận này có thể mở rộng và linh hoạt hơn so với điều phối, nhưng cũng phức tạp hơn trong việc triển khai và bảo trì.   Tuy nhiên, nó cũng có thể linh hoạt hơn vì mỗi dịch vụ có thể phát triển độc lập và lỗi trong một dịch vụ không nhất thiết ảnh hưởng đến toàn bộ hệ thống. -->

<!--  -->

Event-Driven Architecture : https://ddd-practitioners.com/home/glossary/event-driven-architecture  
Entity Identity : https://ddd-practitioners.com/entity-identity  
Event Modeling : https://ddd-practitioners.com/?page_id=994
Event Replay : https://ddd-practitioners.com/?page_id=585
Event Sourced Aggregates : https://ddd-practitioners.com/event-sourcing  
Event Sourcing : https://ddd-practitioners.com/?page_id=581

Eventual Consistency : https://ddd-practitioners.com/?page_id=419

<!-- Example Mapping*   -->
<!-- F -->

Factory : https://ddd-practitioners.com/factory

<!-- Functional Programming*   -->
<!-- G -->

<!-- H -->

Hexagonal Architecture : https://ddd-practitioners.com/hexagonal-architecture  
Highlighted Core : https://ddd-practitioners.com/highlighted-core

<!-- I -->

Identity : https://ddd-practitioners.com/entity-identity

<!-- Impact Mapping*   -->

Infrastructure Service : https://ddd-practitioners.com/infrastructure-service  
Interface Segregation Principle : https://ddd-practitioners.com/?page_id=817

<!-- Inverse Conway Maneuver*   -->
<!-- L -->

Layered Architecture : https://ddd-practitioners.com/layered-architecture  
Liskov Substitution Principle : https://ddd-practitioners.com/home/glossary/liskov-substitution-principle

<!-- Long-running Transaction*   -->
<!-- M -->

Microservices Architecture : https://ddd-practitioners.com/?page_id=398
Module : https://ddd-practitioners.com/?page_id=618
Monolithic Architecture : https://ddd-practitioners.com/?page_id=391

<!-- O -->
<!-- Object-Oriented Programming*   -->
<!-- OLAP*   -->
<!-- OLTP*   -->

Onion Architecture : https://ddd-practitioners.com/home/glossary/onion-architecture

<!-- Open-Closed Principle*   -->

Open-Host Service : https://ddd-practitioners.com/open-host-service  
Optimistic Concurrency Control : https://ddd-practitioners.com/?page_id=609
Orchestration : https://ddd-practitioners.com/?page_id=630

<!-- Outbox Pattern*   -->
<!-- P -->
<!-- Parallel Database*   -->

Partnership : https://ddd-practitioners.com/partnership  
Ports and Adapters : https://ddd-practitioners.com/hexagonal-architecture

<!-- Procedural Programming*   -->
<!-- Projection*   -->

Published Language : https://ddd-practitioners.com/published-language

<!-- Q -->
<!-- Query*   -->

<!-- R -->
<!-- Read Model*   -->
<!-- Refactoring*   -->

Repository : https://ddd-practitioners.com/?page_id=555

<!-- S -->

Saga : https://ddd-practitioners.com/home/glossary/saga  
Segregated Core : https://ddd-practitioners.com/?page_id=378
Separate Ways : https://ddd-practitioners.com/separate-ways  
Service : https://ddd-practitioners.com/service

<!-- Service-Oriented Architecture*   -->

Shared Kernel : https://ddd-practitioners.com/shared-kernel  
Single Responsibility Principle : https://ddd-practitioners.com/single-responsibility-principle  
Snapshots : https://ddd-practitioners.com/snapshots  
SOLID : https://ddd-practitioners.com/home/glossary/solid

<!-- Strangler Fig*   -->

State Stored Aggregates : https://ddd-practitioners.com/state-stored-aggregate  
Strategic Design : https://ddd-practitioners.com/strategic-design  
Strong Consistency : https://ddd-practitioners.com/?page_id=421

<!-- System Event*   -->

<!-- T -->

Tactical Design : https://ddd-practitioners.com/?page_id=453
Test-Driven Development : https://ddd-practitioners.com/test-driven-development

<!-- Transactional Outbox*   -->

<!-- U -->

Ubiquitous Language : https://ddd-practitioners.com/home/glossary/ubiquitous-language

<!-- V -->

Value Object : https://ddd-practitioners.com/home/glossary/value-object  
Vertical Slice Architecture : https://ddd-practitioners.com/home/glossary/vertical-slice-architecture

<!-- W -->
<!-- Wardley Mapping* -->

<!--  -->

Excerpted from [[Domain-Driven Design Book]]

<!-- [[Aggregate]] A cluster of associated objects that are treated as a unit for the purpose of data changes. External references are restricted to one member of the AGGREGATE, designated as the root. A set of consistency rules applies within the AGGREGATE’S boundaries. -->

[[Analysis Pattern]] A group of concepts that represents a common construction in business modeling. It may be relevant to only one domain or may span many domains (Fowler 1997, p. 8).

[[Assertion]] A statement of the correct state of a program at some point, independent of how it does it. Typically, an ASSERTION specifies the result of an operation or an invariant of a design element.

[[Bounded Context]] The delimited applicability of a particular model. BOUNDING CONTEXTS gives team members a clear and shared understanding of what has to be consistent and what can develop independently.

[[Client]] A program element that is calling the element under design, using its capabilities.

[[Cohesion]] Logical agreement and dependence.

[[Command]] (a.k.a. modifier) An operation that effects some change to the system (for example, setting a variable). An operation that intentionally creates a side effect.

[[Context]] The setting in which a word or statement appears that determines its meaning. See [[Bounded Context]].

[[Conceptual Contour]] An underlying consistency of the domain itself, which, if reflected in a model, can help the design accommodate change more naturally.

[[Context Map]] A representation of the [[Bounded Context]]s involved in a project and the actual relationships between them and their models.

<!-- [[Core Domain]] The distinctive part of the model, central to the user’s goals, that differentiates the application and makes it valuable. -->

[[Declarative Design]] A form of programming in which a precise description of properties actually controls the software. An executable specification.

[[Deep Model]] An incisive expression of the primary concerns of the domain experts and their most relevant knowledge. A deep model sloughs off superficial aspects of the domain and naive interpretations.

[[Design Pattern]] A description of communicating objects and classes that are customized to solve a general design problem in a particular context. (Gamma et al. 1995, p. 3)

[[Distillation]] A process of separating the components of a mixture to extract the essence in a form that makes it more valuable and useful. In software design, the abstraction of key aspects in a model, or the partitioning of a larger system to bring the CORE DOMAIN to the fore.

<!-- [[Domain]] A sphere of knowledge, influence, or activity. -->

<!-- [[Domain-Driven Design]] An approach to software development that suggests that (1) For most software projects, the primary focus should be on the domain and domain logic; and (2) Complex domain designs should be based on a model. -->

<!-- [[Domain Expert]] A member of a software project whose field is the domain of the application, rather than software development. Not just any user of the software, the domain expert has deep knowledge of the subject. -->

<!-- [[Domain Layer]] That portion of the design and implementation responsible for domain logic within a LAYERED ARCHITECTURE. The domain layer is where the software expression of the domain model lives. -->

<!-- [[Entity]] An object fundamentally defined not by its attributes, but by a thread of continuity and identity. -->

<!-- [[Factory]] A mechanism for encapsulating complex creation logic and abstracting the type of a created object for the sake of a client. -->

[[Function]] An operation that computes and returns a result without observable side effects.

[[Immutable]] The property of never changing observable state after creation. implicit concept A concept that is necessary to understand the meaning of a model or design but is never mentioned.

[[Intention-Revealing Interface]] A design in which the names of classes, methods, and other elements convey both the original developer’s purpose in creating them and their value to a client developer.

[[Invariant]] An Assertion about some design element that must be true at all times, except during specifically transient situations such as the middle of the execution of a method, or the middle of an uncommitted database transaction.

[[Iteration]] A process in which a program is repeatedly improved in small steps. Also, one of those steps.

[[Large-Scale Structure]] A set of high-level concepts, rules, or both that establishes a pattern of design for an entire system. A language that allows the system to be discussed and understood in broad strokes.

<!-- [[Layered Architecture]] A technique for separating the concerns of a software system, isolating a domain layer, among other things. -->

<!-- [[Life Cycle]] A sequence of states an object can take on between creation and deletion, typically with constraints to ensure integrity when changing from one state to another. May include migration of an [[Entity]] between systems and different [[Bounded Contexts]]. -->

<!-- [[Model]] A system of abstractions that describes selected aspects of a domain and can be used to solve problems related to that domain. -->

<!-- [[Model-Driven Design]] A design in which some subset of software elements corresponds closely to elements of a model. Also, a process of codeveloping a model and an implementation that stay aligned with each other. -->

[[Modeling Paradigm]] A particular style of carving out concepts in a domain, combined with tools to create software analogs of those concepts (for example, object-oriented programming and logic programming).

<!-- [[Repository]] A mechanism for encapsulating storage, retrieval, and search behavior which emulates a collection of objects. -->

[[Responsibility]] An obligation to perform a task or know information (Wirfs-Brock et al. 2003, p. 3).

<!-- [[Service]] An operation offered as an interface that stands alone in the model, with no encapsulated state. -->

[[Side Effect]] Any observable change of state resulting from an operation, whether intentional or not, even a deliberate update.

[[Side Effect Free Function]] See [[Function]].

[[Standalone Class]] A class that can be understood and tested without reference to any others, except system primitives and basic libraries.

[[Stateless]] The property of a design element that allows a client to use any of its operations without regard to the element’s history. A stateless element may use information that is accessible globally and may even change that global information (that is, it may have side effects) but holds no private state that affects its behavior.

<!-- [[Strategic Design]] Modeling and design decisions that apply to large parts of the system. Such decisions affect the entire project and have to be decided at team level. -->

[[Supple Design]] A design that puts the power inherent in a deep model into the hands of a client developer to make clear, flexible expressions that give expected results robustly. Equally important, it leverages that same deep model to make the design itself easy for the implementer to mold and reshape to accommodate new insight.

<!-- [[Ubiquitous Language]] A language structured around the domain model and used by all team members to connect all the activities of the team with the software. -->

[[Unification]] The internal consistency of a model such that each term is unambiguous and no rules contradict.

[[Test-Driven Development]] TDD is a lightweight programming methodology that emphasizes fast, incremental development and especially writing tests before writing code. Ideally these follow one another in cycles measured in minutes. (see full definition under [[Test-Driven Development]] topic)

<!-- [[Value Object]] An object that describes some characteristic or attribute but carries no concept of identity. -->

[[Whole Value]] An object that models a single, complete concept.
